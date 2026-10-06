"""
Prototipo Interactivo de Detección de Intrusiones con Explicabilidad SHAP y Playbooks (OE3)
Tesis: Ciberseguridad para PyMES de Juliaca, Puno - Fernando Ccolla Lazarinos
Seminario de Tesis II (2026-II) - Universidad Nacional de Juliaca
"""

import os
import sys
import time
import json
from flask import Flask, render_template, jsonify, request

# Configuración de rutas y clases auxiliares para el pipeline
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

import __main__
try:
    import run_genis_cleanroom
    __main__.FoldFeatureSelector = run_genis_cleanroom.FoldFeatureSelector
    __main__.SubsampledSMOTE = run_genis_cleanroom.SubsampledSMOTE
except Exception as e:
    # Definiciones de fallback si se ejecuta de forma independiente
    from sklearn.base import BaseEstimator, TransformerMixin
    class FoldFeatureSelector(BaseEstimator, TransformerMixin):
        def fit(self, X, y=None): return self
        def transform(self, X): return X
    class SubsampledSMOTE:
        def fit_resample(self, X, y): return X, y
    __main__.FoldFeatureSelector = FoldFeatureSelector
    __main__.SubsampledSMOTE = SubsampledSMOTE

app = Flask(__name__, template_folder="templates", static_folder="static")

# Diccionario de traducción semántica (Jerga técnica -> Lenguaje PyME)
SEMANTIC_DICTIONARY = {
    "Sdaddr": "Dirección IP origen concentrando tráfico anómalo masivo",
    "Dur": "Duración persistente del flujo de conexión sospechoso",
    "SIntPktMin": "Intervalo ultra acelerado entre paquetes consecutivos",
    "sHops": "Salto de ruta de red foráneo o no habitual",
    "sTtl": "Manipulación del tiempo de vida (TTL) del paquete IP",
    "SrcBytes": "Ráfaga de bytes salientes orientada a sondear puertos",
    "dMaxPktSz": "Paquetes pesados con cargas de autenticación repetitiva",
    "State_CON": "Intentos continuos de apertura y negociación TCP",
    "sMeanPktSz": "Tamaño medio de paquetes en el canal de comunicación",
    "DstWin": "Ventana de recepción saturada en el servidor de destino",
    "AckDat": "Retardo anómalo en confirmaciones de acuse de recibo TCP",
    "DstLoad": "Carga de ancho de banda entrante hacia el host interno"
}

# Base de datos de escenarios de demostración oficiales (Cleanroom Run)
SCENARIOS = {
    "dos": {
        "id": "dos",
        "name": "Ataque de Denegación de Servicio (DoS)",
        "traffic_type": "SYN / UDP Flood masivo hacia gateway local",
        "severity": "CRITICAL",
        "badge_color": "crimson",
        "target_class": "dos",
        "confidence": 0.99995,
        "inference_ms": 18.24,
        "top_shap": [
            {"feature": "Sdaddr", "raw_val": "0.2054", "pct": 42.1, "semantic": SEMANTIC_DICTIONARY["Sdaddr"]},
            {"feature": "Dur", "raw_val": "0.0515", "pct": 28.4, "semantic": SEMANTIC_DICTIONARY["Dur"]},
            {"feature": "SIntPktMin", "raw_val": "0.0472", "pct": 21.5, "semantic": SEMANTIC_DICTIONARY["SIntPktMin"]}
        ],
        "playbook": {
            "code": "PB-01",
            "title": "Protocolo de Mitigación de Saturación de Enlace (DoS)",
            "urgency": "Acción Inmediata (< 30 segundos)",
            "steps": [
                {"num": "1", "action": "Aislar flujo en Gateway / Router MikroTik mediante regla DROP hacia la subred atacante."},
                {"num": "2", "action": "Activar SYN-Cookies y limitar tasa de conexiones simultáneas a 100 conns/segundo."},
                {"num": "3", "action": "Verificar ancho de banda en enlace ISP y confirmar operatividad del sistema de ventas."}
            ],
            "recommended_button": "Aislar IP Atacante en Router"
        }
    },
    "recon": {
        "id": "recon",
        "name": "Reconocimiento y Escaneo de Puertos (PortScan)",
        "traffic_type": "Sondeo horizontal/vertical buscando servicios vulnerables",
        "severity": "WARNING",
        "badge_color": "amber",
        "target_class": "recon",
        "confidence": 1.00000,
        "inference_ms": 18.72,
        "top_shap": [
            {"feature": "sHops", "raw_val": "0.1408", "pct": 47.3, "semantic": SEMANTIC_DICTIONARY["sHops"]},
            {"feature": "sTtl", "raw_val": "0.0857", "pct": 28.8, "semantic": SEMANTIC_DICTIONARY["sTtl"]},
            {"feature": "SrcBytes", "raw_val": "0.0708", "pct": 23.9, "semantic": SEMANTIC_DICTIONARY["SrcBytes"]}
        ],
        "playbook": {
            "code": "PB-02",
            "title": "Protocolo de Aislamiento y Bloqueo de Sondeo (Recon)",
            "urgency": "Acción Preventiva Prioritaria",
            "steps": [
                {"num": "1", "action": "Ocultar puertos abiertos no esenciales (SSH, RDP 3389, Base de datos 3306/5432)."},
                {"num": "2", "action": "Aplicar lista negra temporal (Blacklist 24h) para la dirección externa sospechosa."},
                {"num": "3", "action": "Revisar logs de intentos de autenticación en los servidores contables de la PyME."}
            ],
            "recommended_button": "Cerrar Puertos Expuestos (Blacklist)"
        }
    },
    "bruteforce": {
        "id": "bruteforce",
        "name": "Ataque de Fuerza Bruta (BruteForce)",
        "traffic_type": "Intentos masivos de autenticación contra paneles administrativos",
        "severity": "HIGH",
        "badge_color": "purple",
        "target_class": "bruteforce",
        "confidence": 0.99902,
        "inference_ms": 19.15,
        "top_shap": [
            {"feature": "dMaxPktSz", "raw_val": "0.0674", "pct": 36.8, "semantic": SEMANTIC_DICTIONARY["dMaxPktSz"]},
            {"feature": "Sdaddr", "raw_val": "0.0634", "pct": 34.6, "semantic": SEMANTIC_DICTIONARY["Sdaddr"]},
            {"feature": "State_CON", "raw_val": "0.0524", "pct": 28.6, "semantic": SEMANTIC_DICTIONARY["State_CON"]}
        ],
        "playbook": {
            "code": "PB-03",
            "title": "Protocolo de Blindaje de Credenciales (BruteForce)",
            "urgency": "Acción Crítica Inmediata",
            "steps": [
                {"num": "1", "action": "Bloquear temporalmente intentos fallidos con política de bloqueo tras 3 intentos."},
                {"num": "2", "action": "Activar autenticación de doble factor (2FA / OTP) en cuentas de administradores."},
                {"num": "3", "action": "Forzar cambio preventivo de credenciales en panel ERP/Facturación electrónica."}
            ],
            "recommended_button": "Bloquear IP y Forzar 2FA"
        }
    },
    "benign": {
        "id": "benign",
        "name": "Tráfico Normal de Operación (Benigno)",
        "traffic_type": "Consultas web de facturación, correo y navegación autorizada",
        "severity": "NORMAL",
        "badge_color": "emerald",
        "target_class": "benign",
        "confidence": 0.99998,
        "inference_ms": 17.89,
        "top_shap": [
            {"feature": "sMeanPktSz", "raw_val": "0.0125", "pct": 52.0, "semantic": "Tamaño estándar y predecible de paquetes de red"},
            {"feature": "Dur", "raw_val": "0.0084", "pct": 35.0, "semantic": "Duración normal de sesión de usuario de oficina"},
            {"feature": "AckDat", "raw_val": "0.0031", "pct": 13.0, "semantic": "Tiempos de respuesta óptimos y sin retransmisiones"}
        ],
        "playbook": {
            "code": "PB-00",
            "title": "Monitoreo Estándar de Red",
            "urgency": "Operación Saludable",
            "steps": [
                {"num": "1", "action": "Ninguna acción correctiva requerida. Parámetros dentro de umbrales normales."},
                {"num": "2", "action": "Continuar con la telemetría periódica del sistema de detección."}
            ],
            "recommended_button": "Confirmar Telemetría Normal"
        }
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/scenarios")
def get_scenarios():
    return jsonify(list(SCENARIOS.values()))

@app.route("/api/analyze/<scenario_id>")
def analyze_scenario(scenario_id):
    time.sleep(0.018)  # Simula la latencia individual empírica de 18.8 ms
    scenario = SCENARIOS.get(scenario_id, SCENARIOS["benign"])
    return jsonify(scenario)

@app.route("/api/action", methods=["POST"])
def apply_action():
    data = request.get_json() or {}
    scenario_id = data.get("scenario_id", "unknown")
    action_name = data.get("action", "Mitigación ejecutada")
    reaction_time_sec = data.get("reaction_time_sec", 0.0)
    
    response = {
        "status": "SUCCESS",
        "scenario_id": scenario_id,
        "action_applied": action_name,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "operator_reaction_sec": round(float(reaction_time_sec), 2),
        "gateway_rule": f"/ip firewall filter add chain=forward src-address=192.168.1.105 action=drop comment='IDS-AutoDrop-{scenario_id}'",
        "message": f"Acción defensiva '{action_name}' aplicada correctamente en el gateway perimetral en {reaction_time_sec:.1f} segundos."
    }
    return jsonify(response)

if __name__ == "__main__":
    port = 5000
    print(f"[*] Iniciando Prototipo de Ciberseguridad para PyMES en http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
