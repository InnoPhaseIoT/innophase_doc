const listVersions = [
  {
    'Version': "latest",
    "FreeRTOS-3.0":
      "https://innophase-iot-innophase-doc.readthedocs-hosted.com/en/freertos-3.0",
  },
];

const listModules = [
  {
    'Module': "#",
    "Talaria-TWO": "https://innophase.com/docs/v1.0",
  },
];

export const VersionsList = () => {
  return listVersions;
};

export const ModulesList = () => {
  return listModules;
};
