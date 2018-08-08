import time
import sys

import deeply
from ContentListener import ContentListener

if __name__ == '__main__':
   useCamera = True
   video = ""
   
   if len( sys.argv ) < 2:
      print( "Usage: " + sys.argv[0] + " -c | -v VIDOE_FILE" )
      exit( 1 )
      
   if sys.argv[1] == "-v" and len(sys.argv) == 3:
      useCamera = False
      video = sys.argv[2]
   elif sys.argv[1] == "-c" and len(sys.argv) == 2:
      useCamera = True
   else:
      print("Usage: " + sys.argv[0] + " -c | -v VIDOE_FILE")
      exit( 1 )
   
   print("Using deeply SDK version: " + deeply.GetVersion())
   
   # Get the default camera of your system.
   #if useCamera:
   if useCamera:
      source = deeply.CameraFactory.Instance().CreateDefault()
   else:
      source = deeply.LoadVideoFile( video )
   
   # Create an instance of the FaceProcessorBuilder
   builder = deeply.FaceProcessorBuilder()
   
   # Build the processor with the fluent builder inface.
   processor = builder\
                  .VideoAnalysis()\
                  .SkipFrames(useCamera)\
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
   source.SetOnImageListener( processor )
   
   duration = 10 #s
   if useCamera:
      print( "Starting demo for " + str( duration) + " seconds ..." )
   else:
      print( "Starting demo for " + video )
   
   # Start the camera and grab frames from the webcam
   source.Start()
   
   # The processor gets notified about each new frame form the camera via the method OnImage(...).
   # After processing the processor notifies our ContenListener via OnContent(...).
   
   if useCamera:
      time.sleep( duration )
   else:
      while source.IsPlaying():
         time.sleep( 0.25 )
   
   # Don't forget to stop the camera...
   source.Stop()
   
   print( "Done." )



