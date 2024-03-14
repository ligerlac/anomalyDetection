import FWCore.ParameterSet.Config as cms

CICADA_v1p2p0_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADAModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_v1p2p0_score"),
    treeName = cms.string("CICADA_v1p2p0"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/data_models_30Jan2024/cicada-v1/")
)

CICADA_v2p2p0_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADAModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_v2p2p0_score"),
    treeName = cms.string("CICADA_v2p2p0"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/data_models_30Jan2024/cicada-v2/")    
)

# x.2.0 teacher
CICADA_vXp2p0_Teacher_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADATeacherModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_vXp2p0_teacher_score"),
    treeName = cms.string("CICADA_vXp2p0_teacher"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/data_models_30Jan2024/teacher/")    
)

CICADA_v1p2p0N_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADAModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_v1p2p0N_score"),
    treeName = cms.string("CICADA_v1p2p0N"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/mc_models_05Feb2024/cicada-v1/")
)

CICADA_v2p2p0N_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADAModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_v2p2p0N_score"),
    treeName = cms.string("CICADA_v2p2p0N"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/mc_models_05Feb2024/cicada-v2/")
)

# x.2.0N teacher
CICADA_vXp2p0N_Teacher_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADATeacherModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_vXp2p0N_teacher_score"),
    treeName = cms.string("CICADA_vXp2p0N_teacher"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/mc_models_05Feb2024/teacher/")    
)

#
# Noise suppressed (5 GeV) models
# 

# x.2.1
CICADA_v1p2p1_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADAModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_v1p2p1_score"),
    treeName = cms.string("CICADA_v1p2p1"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/data_models_noiseSuppressed_28Feb2024/cicada-v1/"),
    noiseSuppressionLevel = cms.int32(5),
)

CICADA_v2p2p1_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADAModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_v2p2p1_score"),
    treeName = cms.string("CICADA_v2p2p1"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/data_models_noiseSuppressed_28Feb2024/cicada-v2/")    ,
    noiseSuppressionLevel = cms.int32(5),
)

# x.2.1 teacher
CICADA_vXp2p1_Teacher_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADATeacherModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_vXp2p1_teacher_score"),
    treeName = cms.string("CICADA_vXp2p1_teacher"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/data_models_noiseSuppressed_28Feb2024/teacher/"),
    noiseSuppressionLevel = cms.int32(5),
)

# x.2.1N
CICADA_v1p2p1N_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADAModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_v1p2p1N_score"),
    treeName = cms.string("CICADA_v1p2p1N"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/mc_models_noiseSuppressed_26Feb2024/cicada-v1/"),
    noiseSuppressionLevel = cms.int32(5),
)

CICADA_v2p2p1N_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADAModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_v2p2p1N_score"),
    treeName = cms.string("CICADA_v2p2p1N"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/mc_models_noiseSuppressed_26Feb2024/cicada-v2/"),
    noiseSuppressionLevel = cms.int32(5),
)

# x.2.1N teacher
CICADA_vXp2p1N_Teacher_Ntuplizer = cms.EDAnalyzer(
    'kerasCICADATeacherModelNtuplizer',
    regionToken = cms.InputTag("simCaloStage2Layer1Digis"),
    branchName = cms.string("CICADA_vXp2p1N_teacher_score"),
    treeName = cms.string("CICADA_vXp2p1N_teacher"),
    modelLocation = cms.string("/src/anomalyDetection/paperCode/data/models/mc_models_noiseSuppressed_26Feb2024/teacher/"),
    noiseSuppressionLevel = cms.int32(5),
)
