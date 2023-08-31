const searchElement = document.getElementsByClassName("icon icon-home")[0];

const VersionsList = {
  Version: "latest",
  "1.0.0":
    "https://innophase-iot-innophase-doc.readthedocs-hosted.com/en/v1.0.0",
  "1.0.1":
    "https://innophase-iot-innophase-doc.readthedocs-hosted.com/en/v1.0.1",
};

const ModulesList = {
  Module: "#",
  "Talaria-TWO": "https://innophase-iot-innophase-doc.readthedocs-hosted.com/en/v1.0.0",
};

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
imgElement.src = "_static/download_icon.png";

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
