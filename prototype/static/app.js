// Lógica estricta de monitoreo NIDS-XAI (Alcance de Tesis)

const DATA = {
  recon: {
    badge: "ALERTA",
    severity: "warning",
    title: "Posible reconocimiento de red",
    desc: "Se detectó un patrón compatible con escaneo de puertos o búsqueda de servicios disponibles.",
    meaning: "Un equipo está intentando descubrir qué servicios de su red se encuentran accesibles.",
    actions: [
      "Revisar la dirección de origen.",
      "Bloquear temporalmente si no es reconocida.",
      "Revisar los puertos expuestos.",
      "Verificar servicios sensibles."
    ],
    bullets: [
      { text: "Saltos de red anómalos", tag: "sHops" },
      { text: "Patrón TTL relevante", tag: "sTtl" },
      { text: "Tráfico enviado desde el origen", tag: "SrcBytes" }
    ],
    tech: {
      pred: "Recon",
      conf: "99.9%",
      lat: "18.7 ms",
      shap: "sHops, sTtl, SrcBytes"
    }
  },
  dos: {
    badge: "ALERTA CRÍTICA",
    severity: "danger",
    title: "Posible saturación de servicio de red (DoS)",
    desc: "Se detectó un patrón compatible con saturación de enlace y acumulación atípica de conexiones simultáneas.",
    meaning: "Un equipo externo está transmitiendo ráfagas masivas hacia el enlace de la empresa, lo que puede degradar o interrumpir el acceso a internet.",
    actions: [
      "Revisar la dirección de origen reportada.",
      "Limitar o aislar temporalmente la tasa de peticiones del origen.",
      "Verificar la disponibilidad del enlace con el proveedor de internet.",
      "Comprobar el funcionamiento normal de las terminales de cobro."
    ],
    bullets: [
      { text: "Dirección IP de origen atípica", tag: "Sdaddr" },
      { text: "Persistencia inusual del flujo", tag: "Dur" },
      { text: "Intervalo ultra acelerado entre paquetes", tag: "SIntPktMin" }
    ],
    tech: {
      pred: "DoS",
      conf: ">99.9%",
      lat: "18.2 ms",
      shap: "Sdaddr, Dur, SIntPktMin"
    }
  },
  bruteforce: {
    badge: "ALERTA ALTA",
    severity: "high",
    title: "Posibles intentos repetidos de acceso (BruteForce)",
    desc: "Se detectó un patrón compatible con múltiples intentos sucesivos de autenticación.",
    meaning: "Un cliente externo está enviando solicitudes reiteradas con distintas combinaciones para intentar ingresar a una cuenta protegida.",
    actions: [
      "Revisar la cuenta o panel administrativo consultado.",
      "Bloquear temporalmente los intentos desde la dirección de origen.",
      "Habilitar la verificación en dos pasos (código al celular).",
      "Verificar los registros de intentos de acceso fallidos."
    ],
    bullets: [
      { text: "Cargas útiles de paquete repetitivas", tag: "dMaxPktSz" },
      { text: "Peticiones concentradas hacia el servicio de login", tag: "Sdaddr" },
      { text: "Sesiones TCP consecutivas sin éxito", tag: "State_CON" }
    ],
    tech: {
      pred: "BruteForce",
      conf: "99.9%",
      lat: "19.1 ms",
      shap: "dMaxPktSz, Sdaddr, State_CON"
    }
  },
  benign: {
    badge: "NORMAL",
    severity: "normal",
    title: "Tráfico sin alerta de amenaza",
    desc: "No se detectaron patrones compatibles con las clases de ataque contempladas por el modelo en este flujo.",
    meaning: "El flujo evaluado presenta características de comunicación estándar compatibles con la operación regular del negocio.",
    actions: [
      "Mantener activo el monitoreo de telemetría de red.",
      "No se requiere ninguna acción de bloqueo en este momento."
    ],
    bullets: [
      { text: "Tamaño estándar de paquetes en canal web", tag: "sMeanPktSz" },
      { text: "Duración regular de la transacción", tag: "Dur" },
      { text: "Tiempos normales de acuse de recibo", tag: "AckDat" }
    ],
    tech: {
      pred: "Benign",
      conf: ">99.9%",
      lat: "17.9 ms",
      shap: "sMeanPktSz, Dur, AckDat"
    }
  }
};

let currentKey = "recon";
let techOpen = false;

// Elementos DOM
const flowButtons = document.querySelectorAll(".flow-btn");
const statusBanner = document.getElementById("status-banner");
const statusBadge = document.getElementById("status-badge");
const statusTitle = document.getElementById("status-title");
const statusDesc = document.getElementById("status-desc");
const meaningContent = document.getElementById("meaning-content");
const actionList = document.getElementById("action-list");
const bulletList = document.getElementById("bullet-list");
const btnMarkReviewed = document.getElementById("btn-mark-reviewed");
const btnToggleTech = document.getElementById("btn-toggle-tech");
const reviewStatus = document.getElementById("review-status");
const techBlock = document.getElementById("tech-block");

const techPred = document.getElementById("tech-pred");
const techConf = document.getElementById("tech-conf");
const techLat = document.getElementById("tech-lat");
const techShap = document.getElementById("tech-shap");

function update(key) {
  currentKey = key;
  const d = DATA[key];

  flowButtons.forEach(btn => {
    if (btn.dataset.flow === key) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });

  reviewStatus.style.display = "none";
  btnMarkReviewed.disabled = false;

  // Estado
  statusBanner.className = `status-banner ${d.severity}`;
  statusBadge.textContent = d.badge;
  statusTitle.textContent = d.title;
  statusDesc.textContent = d.desc;
  meaningContent.textContent = d.meaning;

  // Acciones
  actionList.innerHTML = "";
  d.actions.forEach(a => {
    const li = document.createElement("li");
    li.textContent = a;
    actionList.appendChild(li);
  });

  // Factores
  bulletList.innerHTML = "";
  d.bullets.forEach(b => {
    const li = document.createElement("li");
    li.innerHTML = `${b.text} <span class="feat-tag">(${b.tag})</span>`;
    bulletList.appendChild(li);
  });

  // Técnico
  techPred.textContent = d.tech.pred;
  techConf.textContent = d.tech.conf;
  techLat.textContent = d.tech.lat;
  techShap.textContent = d.tech.shap;
}

// Eventos
flowButtons.forEach(btn => {
  btn.addEventListener("click", () => {
    update(btn.dataset.flow);
  });
});

btnMarkReviewed.addEventListener("click", () => {
  btnMarkReviewed.disabled = true;
  reviewStatus.style.display = "block";
});

btnToggleTech.addEventListener("click", () => {
  techOpen = !techOpen;
  if (techOpen) {
    techBlock.style.display = "block";
    btnToggleTech.textContent = "Ocultar detalles técnicos";
  } else {
    techBlock.style.display = "none";
    btnToggleTech.textContent = "Ver detalles técnicos";
  }
});

// Inicializar con Recon
window.addEventListener("DOMContentLoaded", () => {
  update("recon");
});
