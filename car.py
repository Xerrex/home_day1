class Car(object):
    doors=0
    wheels=0

    def __init__(self,name='General',model='GM',type='saloon'):
        self.name = name
        self.model= model
        self.type = type
    #   self.speed = 0
        if (self.name =='Porshe') | (self.name=='Koenigsegg'):
            doors=2
        else:
            doors=4
        self.num_of_doors=doors

        if self.type=='saloon':
            wheels= 4
        else:
            wheels= 8

        self.num_of_wheels = wheels
    #
    # def drive(self,time):
    #     acc=0
    #     acc1= 10
    #     acc2= 1000/3
    #     drive_speed=acc*time
    #     return Car(self.name,self.model,self.vtye,drive_speed)
    #
    def is_saloon(self):
        if self.type =='saloon':
            return True
        else:
            return False







