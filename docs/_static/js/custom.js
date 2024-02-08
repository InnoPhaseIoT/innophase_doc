const searchElement = document.getElementsByClassName("icon icon-home")[0];

const VersionsList = {
    "FreeRTOS-3.0": "https://innophase-iot-innophase-doc.readthedocs-hosted.com/en/freertos-3.0",
    "Versions": "#"
};

const ModulesList = {
    "Talaria-TWO": "https://innophase-iot-innophase-doc.readthedocs-hosted.com/en/freertos-3.0",
    "Modules": "#"
};

let elements = document.querySelectorAll(".imagefiguesclass")
for (let i=0; i<elements.length; i++){
        let elem = elements[i];
        elem.style.textAlign = "center";
        elem.style.font = 'italic 85%/1 arial, sans-serif';

}
// ---------------------------------------------------------------------------------------------------------------------
// hide Prerequisites/evaluation-and-development/power-measurement section:
var prerequisitesSection = document.getElementById('prerequisites');
var evalDevSection = document.getElementById('evaluation-and-development');
var powerMeasureSection = document.getElementById('power-measurement');
var designGuidelinesSection = document.getElementById('design-guidelines');
var inp301xSection = document.getElementById('inp-301x');
var inp3000Section = document.getElementById('inp-3000');
var fotoSection = document.getElementById('foto');
var httpSection = document.getElementById('http');
var mdnsSection = document.getElementById('mdns');
var mqttSection = document.getElementById('mqtt');
var provSection = document.getElementById('prov');
var sntpSection = document.getElementById('sntp');
var sslWrapSection = document.getElementById('ssl-wrap');
var utilsSection = document.getElementById('utils');
var websocketSection = document.getElementById('websocket');
var downloadToolUsageSection = document.getElementById('download-tool-usage');
var usingInp3000ProgrammerBoardSection = document.getElementById('using-inp3000-programmer-board');
var usingUartInterfacesSection = document.getElementById('using-uart-interfaces');
var usingSpiInterfacesSection = document.getElementById('using-spi-interfaces');
var usingJtagAndSwdInterfacesSection = document.getElementById('using-jtag-and-swd-interfaces');
var designSection = document.getElementById('design');
var sampleScenariosSection = document.getElementById('sample-scenarios');
var helpSection = document.getElementById('help');
var appsSection = document.getElementById('apps');
var examplesSection = document.getElementById('examples');


if (prerequisitesSection) {
    prerequisitesSection.style.display = 'none';
}
if (evalDevSection) {
    evalDevSection.style.display = 'none';
}
if (powerMeasureSection) {
    powerMeasureSection.style.display = 'none';
}
if (designGuidelinesSection) {
    designGuidelinesSection.style.display = 'none';
}
if (inp301xSection) {
    inp301xSection.style.display = 'none';
}
if (inp3000Section) {
    inp3000Section.style.display = 'none';
}
if (fotoSection) {
    fotoSection.style.display = 'none';
}
if (httpSection) {
    httpSection.style.display = 'none';
}
if (mdnsSection) {
    mdnsSection.style.display = 'none';
}
if (mqttSection) {
    mqttSection.style.display = 'none';
}
if (provSection) {
    provSection.style.display = 'none';
}
if (sntpSection) {
    sntpSection.style.display = 'none';
}
if (sslWrapSection) {
    sslWrapSection.style.display = 'none';
}
if (utilsSection) {
    utilsSection.style.display = 'none';
}
if (websocketSection) {
    websocketSection.style.display = 'none';
}
if (downloadToolUsageSection) {
    downloadToolUsageSection.style.display = 'none';
}
if (usingInp3000ProgrammerBoardSection){
    usingInp3000ProgrammerBoardSection.style.display = 'none'
}
if (usingUartInterfacesSection){
    usingUartInterfacesSection.style.display = 'none'
}
if (usingSpiInterfacesSection){
    usingSpiInterfacesSection.style.display = 'none'
}
if (usingJtagAndSwdInterfacesSection){
    usingJtagAndSwdInterfacesSection.style.display = 'none'
}
if (designSection){
    designSection.style.display = 'none'
}
if (sampleScenariosSection){
    sampleScenariosSection.style.display = 'none'
}
if (helpSection){
    helpSection.style.display = 'none'
}
if (appsSection) {
    appsSection.style.display = 'none';
}
if (examplesSection) {
    examplesSection.style.display = 'none';
}
// ---------------------------------------------------------------------------------------------------------------------
var selectList = document.createElement("select");
selectList.id = "version-selector";
searchElement.after(selectList);

for (const [key, value] of Object.entries(VersionsList)) {
    var option = document.createElement("option");
    option.value = value;
    option.text = key;
    selectList.appendChild(option);
}

selectList.addEventListener("change", function (e) {
    window.location.href = e.target.value;
});

const moduleElement = document.getElementsByClassName("icon icon-home")[0];
var moduleList = document.createElement("select");
moduleList.id = "module-dropdown";
moduleElement.after(moduleList);

for (const [key, value] of Object.entries(ModulesList)) {
    var moduleopt = document.createElement("option");
    moduleopt.value = value;
    moduleopt.text = key;
    moduleList.appendChild(moduleopt);
}

moduleList.addEventListener("change", function (e) {
    window.location.href = e.target.value;
});

const footerElement = document.getElementsByTagName("footer");
const downloadElement = document.querySelector('[role="contentinfo"]');
var downloadLink = document.createElement("a");
downloadLink.id = "download-pdf-button";
downloadLink.href = "#";
downloadLink.onclick = downloadPDF;

var imgElement = document.createElement("img");
imgElement.src = "https://innophase-iot-innophase-doc.readthedocs-hosted.com/en/freertos-3.0/_static/download_icon.png";

var textNode = document.createTextNode(" Download");

downloadLink.appendChild(imgElement);
downloadLink.appendChild(textNode);

var contentinfoElement = document.querySelector('[role="contentinfo"]');

if (contentinfoElement) {
    contentinfoElement.appendChild(downloadLink);
}

function downloadPDF() {
    window.jsPDF = window.jspdf.jsPDF;
    var docPDF = new jsPDF();
    var htmlFilename = window.location.pathname.split("/").pop();
    var elementHTML = document.querySelector("body");
    docPDF.html(elementHTML, {
        callback: function (docPDF) {
            docPDF.save(htmlFilename + ".pdf");
        },
        x: 0,
        y: 0,
        width: 190,
        windowWidth: 1100,
    });
}

document.addEventListener('DOMContentLoaded', function () {
    // Find the original <li> with class "wy-breadcrumbs-aside"
    var originalLi = document.querySelector('li.wy-breadcrumbs-aside');
    var newImg = document.createElement('img');
    // newImg.src = '_static/logo.png';
    newImg.src = 'https://innophase-iot-innophase-doc.readthedocs-hosted.com/en/freertos-3.0/_static/logo.png';
    newImg.alt = 'Logo';
    newImg.className = 'headerimage';
    originalLi.parentNode.replaceChild(newImg, originalLi);
});

// var parentElement = document.querySelector('.rst-versions').parentNode;
// var divToRemove = document.querySelector('.rst-versions');
// parentElement.removeChild(divToRemove);


// versions, modules dropdown
// prerequisites landing page
// prerequisites Software-page heading on left
// url link wiht be docs-innophaseiot.readthedoc.com
