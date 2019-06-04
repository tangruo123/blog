//当点击顶部按钮的时候，执行方法,scrollTop属性获取选中标签距滚动条的距离。
$('#top').click(function () {
    $('html').animate(
        { scrollTop: '0px' }, 1000
    );
});
//当点击底部标签时候，执行方法，其中offset()获取匹配元素在当前视口的相对偏移,返回的是一个对象，有两个属性top,left
//animate,的第二个属性当然我们也可以设置'slow','normal'或'fast'
$('#foot').click(function () {
    $('html').animate(
        {scrollTop: $('footer').offset().top}, 1000
    );
});