from hamcrest import *
from unittest import TestCase

import deeply

class TestImage( TestCase ):
   def test_CreateImage( self ):
      rgb = deeply.CreateImage( 0, 10, 10, 3, 3, 3*10, 1, deeply.Image.RGB )
      
      assert_that( rgb.GetWidth(), equal_to( 10 ) )
      assert_that( rgb.GetHeight(), equal_to( 10 ) )
      assert_that( rgb.GetPlanes(), equal_to( 3 ) )
      assert_that( rgb.GetPixelFeed(), equal_to( 3 ) )
      assert_that( rgb.GetLineFeed(), equal_to( 30 ) )
      assert_that( rgb.GetPlaneFeed(), equal_to( 1 ) )
      assert_that( rgb.GetColorSpace(), equal_to( deeply.Image.RGB ) )
      
      g = deeply.CreateImage( 0, 100, 100, 1, 1, 100, 0, deeply.Image.GRAYSCALE )
      
      assert_that( g.GetWidth(), equal_to( 100 ) )
      assert_that( g.GetHeight(), equal_to( 100 ) )
      assert_that( g.GetPlanes(), equal_to( 1 ) )
      assert_that( g.GetLineFeed(), equal_to( 100 ) )
      assert_that( g.GetPlaneFeed(), equal_to( 0 ) )
      assert_that( g.GetColorSpace(), equal_to( deeply.Image.GRAYSCALE ) )
      
   def test_AccessDataViaSet( self ):
      rgb = deeply.CreateImage( 0, 10, 10, 3, 3, 3 * 10, 1, deeply.Image.RGB )
      
      for y in range( rgb.GetHeight() ):
         for x in range( rgb.GetWidth() ):
            rgb.Set( x, y, 0, 23 ) # red
            rgb.Set( x, y, 1, 42 ) # green
            rgb.Set( x, y, 2, 128 ) # blue
            
      assert_that( rgb.Get( 0, 0, 0 ), equal_to( 23 ) )
      assert_that( rgb.Get( 0, 9, 0 ), equal_to( 23 ) )
      
      assert_that( rgb.Get( 9, 4, 1 ), equal_to( 42 ) )
      assert_that( rgb.Get( 4, 3, 1 ), equal_to( 42 ) )
      
      assert_that( rgb.Get( 2, 7, 2 ), equal_to( 128 ) )
      assert_that( rgb.Get( 5, 3, 2 ), equal_to( 128 ) )
      