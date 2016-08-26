#Libraries
import os
from os import path
from genericpath import isfile
import shutil
from pydub import AudioSegment

#Scripts
import bpmDetector
import utility

class Place:

    def __init__(self,source,destination):
        self.sourceUrl = source 
        self.destinationUrl = destination
        self.Execute()

    #Song Placer------------------------------------------------------------------------
    def PlaceFile(self,bpm,soruceFilePath):  #return destinationPath
        destinationDirPath = os.path.join(self.destinationUrl,bpm)
        #Check dir Existance
        utility.utCheckDir(destinationDirPath)
        #Move file
        shutil.move(soruceFilePath, destinationDirPath)
    #END Song Placer--------------------------------------------------------------------

    def Execute(self):
        #START---------------------------------------------------------------------------
            #Keep file list
        fileList = os.listdir(self.sourceUrl)
        inputFiles= [ f for f in fileList if os.path.isfile(path.join(self.sourceUrl,f)) ]

            #Initialize Destination Directory
        utility.utCheckDir (self.destinationUrl)

            #CYCLER
        for file in inputFiles:
                #GET SONG PATH
                soruceFilePath  = os.path.join(self.sourceUrl,file)
                print (utility.utGetFileName(file)+"...In Elaborazione")
    
                #GET BPM
                songExtractor = bpmDetector.Detect(soruceFilePath)
                songBpm = songExtractor.extractor()
                print (songBpm)

                #PLACE TO DIR
                self.PlaceFile(str(utility.utRoundup(songBpm)),soruceFilePath)

                print (utility.utGetFileName(file)+"...Elaborato")

        print("end")
        #END-----------------------------------------------------------------------------