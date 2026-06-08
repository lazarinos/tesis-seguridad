const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function downloadPdf(url, outputPath) {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
  });
  const page = await context.newPage();
  
  console.log(`Navigating to ${url}...`);
  
  try {
    const response = await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    const buffer = await response.body();
    
    if (buffer.length < 1000) {
       console.error(`Error: File too small (${buffer.length} bytes). Might be an error page.`);
       await browser.close();
       return false;
    }
    
    fs.writeFileSync(outputPath, buffer);
    console.log(`Success: Saved to ${outputPath} (${buffer.length} bytes)`);
    await browser.close();
    return true;
  } catch (e) {
    console.error(`Error downloading: ${e.message}`);
    await browser.close();
    return false;
  }
}

const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('Usage: node download_helper.js <url> <output_path>');
  process.exit(1);
}

downloadPdf(args[0], args[1]);
