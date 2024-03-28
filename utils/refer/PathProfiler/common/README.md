Whole Slide Image (WSI) Reader
===================================================
The WSI reader (wsi_reader.py) unifies image readers from openslide, tifffile and pixelengine and introduces useful methods to facilitate working with WSIs.  

### Classes 

* `TiffReader(filename)`:  <br>
A WSI reader object from tifffile package.
* `OpenSlideReader(filename)`:  <br>
A WSI reader object from openslide package.
* `IsyntaxReader(filename)`:  <br>
A WSI reader object from pixelengine package.

<b> Function to get the WSI reader based on the image format:
* `get_reader_impl(filename)`:  <br>  </b>
Return a reader object (TiffReader, OpenSlideReader or IsyntaxReader) based on the slide format.
```
Parameter: 
- filename: the slide file to open.
``` 



===================================================
### Properties 

* `level_dimensions`:  A list of (width, height) tuples, indicating the dimensions of slide at each level, i.e. level_dimensions[k] are the dimensions at level k.
* `level_count`:  The number of levels in the slide. Levels are numbered from 0 (highest resolution) to level_count - 1 (lowest resolution).
* `level_downsamples`:  A list of downsample factors for each level of the slide. level_downsamples[k] is the downsample factor of level k.
* `mpp`:  A tuple containing the number of microns per pixel of level 0 in the X and Y dimensions respectively.
* `dtype`:  Type of data
* `n_channels`:  Number of data channels 

===================================================
###  Objects


* `read_region(location, level, tile_size, normalize=True, downsample_level_0=False)` <br>
Returns a tuple of pixel data and alpha mask of the region of the interest (ROI) at the specified level.

```
Parameters: 
- location (tuple): (x, y) the top left pixel position in the level given by parameter "level". 
- level (int): the level number.
- tile_size (tuple): (width, height) the size of the ROI.
- normalize (bool): True to return pixel values in the range of [0-1].
- downsample_level_0 (bool): True to return an image by downsampling ROI from level 0. 
This is added as some slides contain very low quality or compression artefacts at higher levels. 
```

* `read_region_ds(location, downsample, tile_size, normalize=True, downsample_level_0=False)` <br>
Returns a tuple of pixel data and alpha mask of the ROI at the specified downsampled factor with respect to level 0.

```
Parameters: 
- location (tuple): (x, y) the top left pixel position in the downsampled slide. 
- downsample (float): downsample factor with respect to the image at level 0.
- tile_size (tuple): (width, height) the size of the ROI.
- normalize (bool): True to return pixel values in the range of [0-1].
- downsample_level_0 (bool): True to return an image by downsampling ROI from level 0. 
This is added as some slides contain very low quality or compression artefacts at higher levels. 
```

* `get_downsampled_slide(size)`   <br>
Returns a tuple of pixel data and alpha mask of the slide thumbnail of the specified size. <br>
```
Parameters: 
- size (tuple): The size of the slide thumbnail as (width, height). 
``` 

* `get_best_level_for_downsample(downsample)` <br>
Returns the best level for the given downsample factor.
```
Parameters: 
- downsample (float): The downsampling factor.
``` 

===================================================

### Examples 

``` shell
reader=get_reader_impl(filename)
slide=reader(filename)
tile, alpha_mask=slide.read_region_ds((1000,1000), 2**3, (512, 512), normalize=False, downsample_level_0=False)
```
More usage examples can be found in "common/tile_processing_parallel.py" and "quality-assessment/run.py".
