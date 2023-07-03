jQuery(document).ready(function ($) {

    // Do stuff here

        var menu = $('body');
		var origOffsetY = menu.offset().top;

		function scroll() {
			if ($(window).scrollTop() >= origOffsetY + 10) {
				$('#nav-main').addClass('nav-scroll-off');
			} else {
				$('#nav-main').removeClass('nav-scroll-off');
			}


		}

		document.onscroll = scroll;





		$('.grid').isotope({
			layoutMode: 'packery',
			packery: {
				columnWidth: '.grid-sizer'
				},
			itemSelector: '.grid-item',
			percentPosition: true

		  });


		  $(document).ready(function(){
			$(".owl-carousel").owlCarousel();
		  });

		  $('#homeSlides.owl-carousel').owlCarousel({
			items:1,
			loop:true,
			margin:0,
			nav:false,
			autoplay:true,
			autoplayTimeout:3000,
			autoplayHoverPause:false
		})
		$('#testimonialCarousel').owlCarousel({
			items:1,
			loop:true,
			margin:0,
			nav:true,
			autoplay:true,
			autoplayTimeout:9000,
			autoplayHoverPause:false
		})
	
	
	   $('.btn-apply').on("click", function(){ gtag_report_conversion(url); });



		//$('body.page-id-4712 .job_cat_single a').click(function(e) {
			//e.preventDefault();
		//	var pageurl = $(this).attr('href');
		//	$("#iframe iframe").attr("src", pageurl);

		//	$([document.documentElement, document.body]).animate({
				//scrollTop: $("#iframe").offset().top - 140}, 1500);
		//});
	
	
	
		//var getUrlParameter = function getUrlParameter(sParam) {
		//var sPageURL = window.location.search.substring(1),
		//	sURLVariables = sPageURL.split('&'),
		//	sParameterName,
		//	i;

		//for (i = 0; i < sURLVariables.length; i++) {
		//	sParameterName = sURLVariables[i].split('=');

		//	if (sParameterName[0] === sParam) {
		//		return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
		//	}
		//}
		//return false;
		//};
	
	
		//var jobarea = getUrlParameter('area');
		//if(jobarea) {
		//	$([document.documentElement, document.body]).animate({
		//		scrollTop: $("#iframe").offset().top - 140}, 1500);
		//}
		//if(jobarea === "healthcare") {
				//$("#iframe iframe").attr("src", "https://jobboard.ontempworks.com/Trinity/Jobs/Search?Keywords=%22Healthcare%22");
		//}
		//if(jobarea === "industrial") {
				//$("#iframe iframe").attr("src", "https://jobboard.ontempworks.com/Trinity/Jobs/Search?Keywords=%22Industrial%22");
		//}
		//if(jobarea === "admin") {
				//$("#iframe iframe").attr("src", "https://jobboard.ontempworks.com/Trinity/Jobs/Search?Keywords=%22Admin%2FClerical%22");
		//}
		//if(jobarea === "manufacturing") {
				//$("#iframe iframe").attr("src", "https://jobboard.ontempworks.com/Trinity/Jobs/Search?Keywords=%22Manufacturing%22");
		//}
		//if(jobarea === "finance") {
				//$("#iframe iframe").attr("src", "https://jobboard.ontempworks.com/Trinity/Jobs/Search?Keywords=%22Finance%22");
		//}



}); // jQuery End
