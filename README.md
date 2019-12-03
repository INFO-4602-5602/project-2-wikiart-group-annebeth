# Project description

## Overview
For these two visualizations, I decided to focus on Renaissance and Post-Renaissance painting.
The first visualization gives an overview of different style periods; showing a rough timeline for each
and also showing overlap between different styles. The second visualization allows users to explore
these different styles more, by looking at specific artists and their paintings within the period.

The first visualization is implemented as a stacked area chart. In some cases, these can be tricky because they do
not allow for good comparison of values. In this case, I was much more interested in a rough overview of the
time periods, which is why I did not even include labels on the y-axis. For a user exploring this information, it is much more interesting to look at the differences between areas than to look at how many painting were painted exactly
in 1886.

The second visualization is implemented as a zoomable circle packing. It consists of different hierarchical levels:
the style, the artists within that style and the paintings created by those artists. The colors of the circles correspond with the legend in the first visualization.

## Implementation
#### Preprocessing
For both visualizations, the data was preprocessed with the [preprocess_category_data](https://github.com/INFO-4602-5602/project-2-wikiart-group-annebeth/blob/master/preprocess_category_data.py) script. For the first visualization,
I simply collected counts per year for all the different style categories. For the second visualization, I created
a JSON file that describes the hierarchy from style period > artist > paintings.

#### Interaction
Each of the visualizations is interactive. In the first visualization, hovering over the legend will highlight
the corresponding area. The second visualization has a zoom function and a tooltip. The tooltip shows different
levels of information for the different levels of circles. The zoom (activated by clicking on a circle) lets a user explore a specific section in more detail. Try to click while holding ALT for a special effect!

## Design process and roles
Since I worked alone, I will skip discussing roles here.

For designing these visualizations, I went through an iterative design process. Originally, I was planning
to add tiny images of the paintings in the white circles in the second visualization, but unfortunately that
made the visualization extremely slow. Since this visualization is set up for exploration and discovery, having
the images in the second visualization would have made that element much stronger.

## Running the project
This project can be run in the browser by cloning the Github project or by downloading the zipped folder. Although the visualizations depend on preprocessed data, that data is available in the folder [preprocessed_data](https://github.com/INFO-4602-5602/project-2-wikiart-group-annebeth/tree/master/data). By using the project folder as the root folder and running a server (for example: `python -m SimpleHTTPServer`), the visualizations should be visible on [localhost](http://localhost:8000/).

## Sources
To implement this project, I looked at various sources. Below is a link to the sources and a short description of which part of the source were used:

- A lot of the code for the zoomable circle packing comes from: https://gist.github.com/mbostock/7607535.
- Inspiration for the stacked area chart comes from: https://www.d3-graph-gallery.com/graph/stackedarea_template.html.
