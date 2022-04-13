new TypeIt("#index-center-1-typo", {
    speed : 50,
    startDelay : 900,
})
.type("Do you want to edit your image?", {delay: 100})
.type("<br>Search Editor", {delay: 300})
.delete(6, {delay:200})
.type("<string style='color:pink;'>SMLN!</strong>")
.go();

setTimeout(() => {
    new TypeIt("#formElement", {
        strings: "   SMLN",
        waitUntilVisible: true,
    }).go();
},4100);
