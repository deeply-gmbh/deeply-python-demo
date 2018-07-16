import time

import deeply
from ContentListener import ContentListener

if __name__ == '__main__':
   print("Using deeply SDK version: " + deeply.GetVersion())
   
   # Get the default camera of your system.
   camera = deeply.CameraFactory.Instance().CreateDefault()
   
   # Create an instance of the FaceProcessorBuilder
   builder = deeply.FaceProcessorBuilder()
   
   # Build the processor with the fluent builder inface.
   processor = builder\
                  .VideoAnalysis()\
                  .SearchEyes( True )\
                  .AnalyzeGender( True )\
                  .AnalyzeAge( True )\
                  .AnalyzeHappy( True )\
                  .Build()
   
   # Create an instance of the custom content listener.
   contentListener = ContentListener()
   
   # Set the new listener
   processor.SetOnContentListener( contentListener )
   
   # Set the processor as image listener in the camera.
   camera.SetOnImageListener( processor )
   
   duration = 10 #s
   print( "Starting demo for " + str( duration) + " seconds ..." )
   
   # Start the camera and grab frames from the webcam
   camera.Start()
   
   # The processor gets notified about each new frame form the camera via the method OnImage(...).
   # After processing the processor notifies our ContenListener via OnContent(...).
   
   time.sleep( duration )
   
   # Don't forget to stop the camera...
   camera.Stop()
   
   print( "Done." )



