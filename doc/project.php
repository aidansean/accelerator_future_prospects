<?php
include_once($_SERVER['FILE_PREFIX']."/project_list/project_object.php") ;
$github_uri   = "https://github.com/aidansean/accelerator_future_prospects" ;
$blogpost_uri = "http://aidansean.com/projects/?tag=accelerator_future_prospects" ;
$project = new project_object("accelerator_future_prospects", "Accelerator future prospects", "https://github.com/aidansean/accelerator_future_prospects", "http://aidansean.com/projects/?tag=accelerator_future_prospects", "/~aidanrandle-conde/aidansean/advent2012/images/project.jpg", "/~aidanrandle-conde/aidansean/advent2012/images/project_bw.jpg", "This project was written as part of the content for a talk presented at the International Workshop on Future Linear Colliders to compare the future prospects of the LHC and lepton colliders.  It is shared here in case it is of use for other physicists.", "", "") ;
?>