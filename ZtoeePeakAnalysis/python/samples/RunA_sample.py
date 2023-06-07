#!/usr/bin/env python3
from .sample import sample
import os

hdfsPath = "/hdfs/store/user/aloeliger/Ztoee_wminiCICADA/v_1/RunA/"

theFiles = []
chains = [
    'basicEventInfoAnalyzer/basicInfo',
    'miniCICADAAnalyzer/miniCICADAScoreTree',
    'electronInformationAnalyzer/ElectronInformation'
]

for root, dirs, files in os.walk(hdfsPath, topdown=True):
    for name in files:
        theFiles.append(os.path.join(root, name))

RunASample = sample(
    listOfFiles=theFiles,
    listOfChains=chains,
)