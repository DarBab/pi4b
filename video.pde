
int [] bl = [500];
int cnt = 1000;

class Ball{
   float x,y,xm,ym,tsz;
   color cr;
   Ball(float xc, float yc, float xs, float ys,color c,float sz){
      x=xc;
      y=yc;
      xm=xs;
      ym=ys;
      cr=c;
      tsz=sz;
      
   }
   
   void show(){
      fill(cr);
      ellipse(x,y,tsz,tsz);
      x+=xm;
      y+=ym;
   }
   
   void check(){
      if (x>=screenWidth){
         x=screenWidth;
         xm=-xm;
      }
      if (x<=0){
         x=0;
         xm=-xm;
         
      }
      if (y>=screenHeight){
         y=screenHeight;
         ym=-ym;
      }
      if (y<=0){
         y=0;
         ym=-ym;
      }
   }
   
   void drop(){
      xm = 0;
      ym = 0;
   }
}








void setup() {
   size(screenWidth, screenHeight,);
   for (int i=0;i<400;i=i+1){
      z=random(50);
      w=random(screenWidth);
      h=random(screenHeight);
      dx=random(-10,10);
      dy=random(-10,10);
      r=random(255);
      g=random(255);
      b=random(255);
      all=color(r,g,b);
      bl[i]=new Ball(w,h,dx,dy,all,z);
   }
}



void draw() {
   background(0,0,2555);
   cnt = cnt - 1;
   
   for (int j=0;j<300;j=j+1){
      bl[j].show();
      bl[j].check();
      if (cnt <= 0){
         fall();
      }
      
      
   }
   
}

void fall() {
   for (int j=0;j<300;j=j+1){
      bl[j].drop();
   }
}




