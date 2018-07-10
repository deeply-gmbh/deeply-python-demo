import deeply

# Simple implementation of the OnContentListener callback interface.
class ContentListener( deeply.OnContentListener ):
   def __init__( self ):
      super( ContentListener, self ).__init__()
   
   # Called everytime the processor has new results.
   def OnContent( self, content, image ):
      print( "#Objects: " + str( content.GetObjectCount() ) )
      
      for i in range( content.GetObjectCount() ):
         o = content.GetObject( i )
         print( " * " + o.GetAttributeByKey( "Gender") + " "
                      + o.GetAttributeByKey( "Age" ) + " - "
                      + "Happy: " + str( o.GetRatingByKey( "Happy" ) ) )
   