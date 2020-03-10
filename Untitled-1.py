from tkinter import Tk, Canvas
import random




#pars
w=1024
h=768
segment_size=20
in_game=True

def create_eat(self):
        global blockToEat 
        posx=segment_size*(random.randint(1,(w-segment_size)/segment_size))  
        posy=segment_size*(random.randint(1,(h-segment_size)/segment_size))

        blockToEat=c.create_oval(
            posx,
            posy,
            posx+segment_size,
            posy+segment_size,
            fill='red'
        )

def main():
    global in_game

    if in_game:
        s.move() 

        head_crds=c.coords(s.segments[-1].instance)
        x1,y1,x2,y2=head_crds

        if x1<0 or x2>w or y1<0 or y2>h:
            in_game=False

        elif head_crds == c.coords(blockToEat):
            s.add_seg()
            c.delete(blockToEat)
            c.create_eat()

        else:
            for index in range(len(s.segments)-1):
                if c.coords(s.segments[index].instance)==head_crds:
                    in_game=False

    else:
        c.create_text(w/2,
        h/2,
        text='potracheno',
        font='GTA Russian Regular 20',
        fill='#ff0000'
        )   
    c.bind('<KeyPress>',s.change_direction)    

class Segment(object):
    def __init__(self,x,y):
        self.instance=c.create_rectangle(
        x,
        y,
        x+segment_size,
        y+segment_size,
        fill='white'    
        )

class Snake(object):
    def __init__(self, segments):
         self.segments=segments

         #move
         self.mapping={
         'down':(0,1),
         'up':(0,-1),
         'left':(-1,0),
         'right':(1,0)    
         }
         #right for start
         self.vector=self.mapping['right']

    def move(self):
        #move the snake

        #for all segs without 1st
        for index in range (len(self.segments)-1):
            segment=self.segments[index].instance
            x1,y1,x2,y2=c.coords(self.segments[index+1].instance) 
            #change every seg position to second seg position
            c.coords(segment,x1,y1,x2,y2) 
        #get coords from 2nd seg from head
        x1,y1,x2,y2=c.coords(self.segments[-2].instance)

        #take head to the go vector
        c.coords(self.segments[-1].instance,
        x1+self.vector[0]*segment_size,
        y1+self.vector[1]*segment_size,
        x2+self.vector[0]*segment_size,
        y2+self.vector[1]*segment_size
        ) 
  
    def change_direction(self, event):
        #event=pushed button
        if event.keysym in self.mapping:
            self.vector=self.mapping[event.keysym]

    def add_seg(self):
        last_seg=c.coords(self.segments[0].instance)
        #crds for new swg
        x=last_seg[2]-segment_size
        y=last_seg[3]-segment_size

        #add seg
        self.segments.insert(0,Segment(x,y))           


root=Tk()
root.title('kobrenok')

#paint
c=Canvas(root, width=w, height=h, bg="#003300")
c.grid()

#create pack of segs
segments=[Segment(segment_size,segment_size),
    Segment(segment_size*2,segment_size),
    Segment(segment_size*3,segment_size)
]    
s=Snake(segments)   
        
#focus for presses
c.focus_set()
main()
root.mainloop()

