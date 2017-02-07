<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta http-equiv="x-ua-compatible" content="ie=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" />
<title>Magic Mirror</title>

<link rel="stylesheet" href="./assets/stylesheets/demo.css" />
<link rel="stylesheet" href="./css/unsemantic-grid-responsive.css" />
<link rel="stylesheet" href="./css/magicmirror.css" />

</head>
<body >
<?php date_default_timezone_set('Asia/Kolkata'); ?>


<div class="grid-container  ">

	<div class="grid-100  textcolorvisible">
		<div class="verybigfont" id='timeHolder'>
			<?php 			
				$today = date("g:i a");   
				print($today)
			?>
		</div>
		<div class="averagefont" id="dateHolder">
		<b>
			<?php
				$today = date("l, M jS");   
				print($today)
			?>
		</b>
		</div>
	</div>
	
  
 
</div>

<div class="grid-container">
	<div class="grid-10">&nbsp;</div>
	<div class="grid-80  textcolorvisible rightAlign"><hr></hr></div>
	<div class="grid-10">&nbsp;</div>
</div>

<div class="grid-container  ">
	<div class="grid-30">
			<div>
				<img src='./images/sun.png' height='90px'/>
			</div>
			<div class="averagefont textcolorvisible">
				Sunny
			</div>
	</div>
	<div class="grid-30  textcolorvisible">
		<div>
				<img src='./images/temperature.png' height='90px'/>
		</div>
		<div class="averagefont textcolorvisible">
				26°C
		</div>
	</div>
	<div class="grid-40  textcolorvisible rightAlign">
		&nbsp;
	</div>
  
 
</div>




<div class="grid-container">
	<div class="grid-10">&nbsp;</div>
	<div class="grid-80  textcolorvisible rightAlign"><hr></hr></div>
	<div class="grid-10">&nbsp;</div>
</div>

<div class="grid-container">
	<div class="grid-100 textcolorvisible tinyfont leftAlign">
	<div class="puzzleDiv">Q: I’m tall when I’m young and I’m short when I’m old. What am I?</div>
	

<div class="puzzleDiv">Q: In a one-story pink house, there was a pink person, a pink cat, a pink fish, a pink computer, a pink chair, a pink table, a pink telephone, a pink shower– everything was pink! What color were the stairs?
</div>

<div class="puzzleDiv">Q: What has hands but can not clap?
</div>

<div class="puzzleDiv">Q: A house has 4 walls. All of the walls are facing south, and a bear is circling the house. What color is the bear?
</div>

<div class="puzzleDiv">Q: What is at the end of a rainbow?</div>

	</div>
</div>

<div class="grid-container">
	<div class="grid-10">&nbsp;</div>
	<div class="grid-80  textcolorvisible rightAlign"><hr></hr></div>
	<div class="grid-10">&nbsp;</div>
</div>
  
  <script src="./assets/javascripts/jquery.js"></script>
  <script src="./assets/javascripts/demo.js"></script>
  <script src="./js/magicmirror.js"></script>
  

</body>
</html>