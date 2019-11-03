
var canvas, ctx, flag = false,
                prevX = 0,
                currX = 0,
                prevY = 0,
                currY = 0,
                dot_flag = false;

            var x = "red",
                y = 3;

            function init() {
                canvas = document.getElementById('layer2');
                ctx = canvas.getContext("2d");
                w = canvas.width;
                h = canvas.height;
            }
            

            function draw(path) {
		    var prevX = path[0][0];
		    var prevY = path[0][1];
		    var myLen = path.length;
		    for(var i=1;i<myLen;i++){
			currX=path[i][0];
			currY=path[i][1];
		    	ctx.beginPath();
                	ctx.moveTo(prevX, prevY);
                	ctx.lineTo(currX, currY);
                	ctx.strokeStyle = x;
                	ctx.lineWidth = y;
                	ctx.stroke();
                	ctx.closePath();
			prevX = currX;
			prevY = currY;
		    }
                
            }


        var canvas = document.getElementById("layer1"),
                ctx = canvas.getContext("2d"),
                image = document.getElementById("../../../wegmansUncropped");

        canvas.height = 495;
        canvas.width = 782;
        ctx.drawImage(image,0,0);

        var imgd = ctx.getImageData(0, 0, 782, 495),
                pix = imgd.data,
                newColor = {r:0,g:0,b:0, a:0};

 for (var i = 0, n = pix.length; i <n; i += 4) {
            var r = pix[i],
                        g = pix[i+1],
                        b = pix[i+2];

                // If its white then change it
                if(r == 255 && g == 255 && b == 255){
                        // Change the white to whatever.
                        pix[i] = newColor.r;
                        pix[i+1] = newColor.g;
                        pix[i+2] = newColor.b;
                        pix[i+3] = newColor.a;
                }
        }

ctx.putImageData(imgd, 0, 0);<200b>

