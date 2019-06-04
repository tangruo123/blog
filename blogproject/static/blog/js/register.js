/*
var = $("input[name=password]").blur(function(){
  alert($(this).val())
})
*/
// 获取两次输入的密码
var1 = $("input[name=password]").val();
var2 = $("input[name=password2]").val();

// 当两次密码不同时提示，并清除密码
$("input[name=password2]").blur(function(){
    if(var1!=var2){
        alert("两次输入的密码不相同，请重新输入！");
        $("input[name=password]").val("");
        $("input[name=password2]").val("");
    }
});
