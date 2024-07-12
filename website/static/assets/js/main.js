//home.html
document.addEventListener("DOMContentLoaded", function(){//JavaScript code listens for the "DOMContentLoaded" event to ensure that the document is fully loaded before executing
    var sentences=document.getElementsByClassName("welcome");//in html file, set up an id# named "sentence", now let me retrieve this thing by its id#
    var index = 0;
    // var charIndex = 0;
    // var sentenceIndex = 0;
    // var sentenceElement = document.getElementById("sentence"); )
  
    function typeSentence(){ //the function body of typeSentence()
      if(index < sentences.length){//sentenceIndex: is each sentence's index #
        var sentence = sentences[index];
        var chars = sentence.textContent.split("");
        sentence.textContent="";//.textContent is used to access or modify the text content of an element once it has been selected.
        sentence.style.fontFamily=""; //reset font before typing
        
        var charIndex = 0;
        var typeInterval = setInterval(function(){
          if(charIndex < chars.length){
            sentence.textContent += chars[charIndex];
            charIndex++;
          }
          else{
            clearInterval(typeInterval);
            index++;
            typeSentence();
          }
        }, 50);    
        sentence.style.opacity="1";
      }
    }
    typeSentence(); //call the function
    });
  
  
  //about.html
  //the js part is used to display character by character one by one on the screen, the actual effect of blinking
  //cursor (its size, thickness, how fast it blinks)
  document.addEventListener("DOMContentLoaded", function(){//JavaScript code listens for the "DOMContentLoaded" event to ensure that the document is fully loaded before executing
    var sentences=document.getElementsByClassName("para");//in html file, set up an id# named "sentence", now let me retrieve this thing by its id#
    var index = 0;
    // var charIndex = 0;
    // var sentenceIndex = 0;
    // var sentenceElement = document.getElementById("sentence"); )
  
    function typeSentence(){ //the function body of typeSentence()
      if(index < sentences.length){//sentenceIndex: is each sentence's index #
        var sentence = sentences[index];
        var chars = sentence.textContent.split("");
        sentence.textContent="";//.textContent is used to access or modify the text content of an element once it has been selected.
        
        var charIndex = 0;
        var typeInterval = setInterval(function(){
          if(charIndex < chars.length){
            sentence.textContent += chars[charIndex];
            charIndex++;
          }
          else{
            clearInterval(typeInterval);
            index++;
            typeSentence();
          }
        }, 50);    
        sentence.style.opacity="1";
      }
    }
    typeSentence(); //call the function
    });



// Function to update likes count
function like(projectId) {
  $.ajax({
      url: '/projects/like/' + projectId + '/',
      // url: '{% url "like_project" project_id=0 %}'.replace('0', projectId),
      type: 'GET',
      success: function(data) {
          $('#clicklikes' + projectId).text(data.likes + ' like(s)');
      }
  });
}

