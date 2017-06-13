class Car(object):
    #doors=0
    #wheels=0

    def __init__(self,name='General',model='GM',type='saloon',speed=0):
        self.name = name
        self.model= model
        self.type = type
        self.speed =speed

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



    def drive(self,time):
        if self.type == 'saloon':
            drive_speed= (1000/3)*time
        else:
            drive_speed = 11*time

        self.speed=drive_speed


        return Car(self.name,self.model,self.type, drive_speed)



    def is_saloon(self):
        if self.type =='saloon':
            return True
        else:
            return False







