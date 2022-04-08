var editor = new tui.ImageEditor('#tui-image-editor', {

    cssMaxWidth: 500,
    cssMaxHeight: 700,
    usageStatistics: false,
    
  });



/*
 setTimeout(() => {
  
 }, 1000);
 */
 function addIcon_arrow(){  
  editor.addIcon('arrow');
}

function addShape_rect(){  
  console.log("rect");
  editor.addShape('rect', {
    stroke: 'black',
    strokeWidth: 3,
    width: 50,
    height: 50,
    left: 140,
    top: 70,
    isRegular: false
});
}
function addShape_circle(){  
  editor.addShape('circle', {
    
    stroke: 'black',
    strokeWidth: 3,
    rx: 30,
    ry: 30,
    isRegular: false
});
}
function addShape_triangle(){  
  editor.addShape('triangle', {

    stroke: 'black',
    strokeWidth: 3,
    width: 50,
    height: 50,
    left: 140,
    top: 70,
    isRegular: false
});
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

