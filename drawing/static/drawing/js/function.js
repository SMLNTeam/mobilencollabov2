import editor from "./base.js";


 function addIcon_arrow(){  
    editor.addIcon('arrow');
  }
  
  function addShape_rect(){  
    editor.addShape('rect');
  }
  function addShape_circle(){  
    editor.addShape('circle', {

      stroke: 'black',
      strokeWidth: 3,
      rx: 10,
      ry: 100,
      isRegular: false
  });
  }
  function addShape_triangle(){  
    editor.addShape('triangle');
  }
  function addText(){
    editor.addText('abcd', {
      styles: {
          fill: '#000',
          fontSize: 20,
          fontWeight: 'bold'
      },
      position: {
          x: 100,
          y: 100
      }
  }).then(objectProps => {
      console.log(objectProps.id);
  });
  }

