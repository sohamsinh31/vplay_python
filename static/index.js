$(document).ready(function(){
    $("#b1").on("change",function(){
        $.ajax({
            url:'',
            type:'get',
            data: {
                btext:$(this).val()
            },
            success:function(responce){
                $("#b2").data(responce)
            }
        });
    });
});