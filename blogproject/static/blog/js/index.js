//  第一张轮播图设为可见
$("#myCarousel .item").first().addClass("active");
//  第一个点设为实心
$("#myCarousel .active1").first().addClass("active");
// 轮播图滚动间隔时间
$('.carousel').carousel({
  interval: 5000
})