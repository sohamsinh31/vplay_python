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
let input, hashtagArray, container, t;

input = document.querySelector('#hashtags');
container = document.querySelector('.tag-container');
hashtagArray = [];

input.addEventListener('keyup', () => {
    if (event.which == 13 && input.value.length > 0) {
      var text = document.createTextNode(input.value);
      var p = document.createElement('p');
      container.appendChild(p);
      p.appendChild(text);
      p.classList.add('tag');
      input.value = '';

      let deleteTags = document.querySelectorAll('.tag');

      for(let i = 0; i < deleteTags.length; i++) {
        deleteTags[i].addEventListener('click', () => {
          container.removeChild(deleteTags[i]);
        });
      }
    }
});
$("#tags").on('click',function(e){
    e.preventDefault();
    let val = $("#hashtag").val();

})