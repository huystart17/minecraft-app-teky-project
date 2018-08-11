class Building():

    def __init__(self,mc,x,y,z):

        self.mc=mc

        self.x=x

        self.y=y

        self.z=z

    def small_house(self):

        x=self.x

        y=self.y

        z=self.z

        mc =self.mc

        mc.setBlocks(x,y-1,z,x+10,y+5,z+10,155)

        mc.setBlocks(x+1,y,z+1,x+9,y+4,z+9,0)



        #den

        mc.setBlocks(x+9,y,z+1,x+9,y,z+1,89)

        mc.setBlocks(x+7,y,z+9,x+9,y+4,z+9,89)

        #cua

        mc.setBlocks(x,y,z+5,x,y+1,z+5,0)

        mc.setBlocks(x,y+1,z+5,x,y+1,z+5,64,8)

        mc.setBlocks(x,y,z+5,x,y,z+5,64)

        mc.setBlocks(x-1,y-1,z+5,x-1,y-1,z+5,156)

        #cua so

        mc.setBlocks(x,y+2,z+2,x,y+3,z+3,102)

        mc.setBlocks(x,y+2,z+7,x,y+3,z+8,102)



        #ruong

        mc.setBlocks(x+4,y,z+9,x+3,y,z+9,54)

        mc.setBlocks(x+7,y,z+1,x+8,y,z+1,54)

        mc.setBlocks(x+7,y+1,z+1,x+8,y+1,z+1,96,1)

        #ban che tao

        mc.setBlocks(x+6,y,z+9,x+6,y,z+9,58)



        #lo ren

        mc.setBlocks(x+5,y,z+9,x+5,y+1,z+9,61)



        #giuong

        mc.setBlocks(x+7,y+1,z+2,x+7,y+1,z+2,26,7)

        mc.setBlocks(x+8,y+1,z+2,x+8,y+1,z+2,26,11)

        mc.setBlocks(x+7,y,z+3,x+9,y,z+2,5,5)

        mc.setBlocks(x+6,y,z+3,x+6,y,z+1,53)



        #ban

        mc.setBlocks(x+4,y,z+3,x+4,y,z+1,126,2)



        #sach

        mc.setBlocks(x+7,y+1,z+9,x+9,y+3,z+9,47)

    def big_house(self):

        x=self.x

        y=self.y

        z=self.z

        mc =self.mc

        #1

        mc.setBlocks(x,y-1,z,x+10,y+5,z+10,155)

        mc.setBlocks(x+1,y,z+1,x+9,y+4,z+9,0)



        #2...

        mc.setBlocks(x+3,y+6,z,x+10,y+11,z+10,1)

        mc.setBlocks(x+1,y+6,z+1,x+8,y+10,z+9,0)

        #ban cong

        mc.setBlocks(x,y+6,z,x+1,y+6,z+10,85)









        #cua

        mc.setBlocks(x,y,z+5,x,y+1,z+5,0)

        mc.setBlocks(x,y+1,z+5,x,y+1,z+5,64,8)

        mc.setBlocks(x,y,z+5,x,y,z+5,64)