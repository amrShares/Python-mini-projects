# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:32:38 2022

@author: amrsh
"""
#    moods = ("tired", "happy", "lazy")

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

disgust = mpimg.imread('disgust.jpg')
happy  = mpimg.imread('happy.jpg')
lazy  = mpimg.imread('lazy.jpg')
driving  = mpimg.imread('driving.jpg')
scarred  = mpimg.imread('scarred.jpg')

class Person:
    
    def __init__(self, name = None, money = 0, mood = None, health_rate = 0 ):
        self.name = name
        self.money = min(money, 1000)
        self.mood = mood
        self.health_rate = min(max(health_rate, 0), 100)
        
    def sleep(self, amount):
        
        if amount < 7:
            self.mood = "tired"
            plt.imshow(disgust)
            plt.show()
        elif amount == 7:
            self.mood = "happy"
            plt.imshow(happy)
            plt.show()
        else :
            self.mood = "lazy"
            plt.imshow(lazy)
            plt.show()
            
    def eat(self, no_of_meals):
        self.health_rate = (25*(1 + no_of_meals)) % 100
            
    def buy(self, no_of_items):
        if self.money - 10 * no_of_items >= 0:
            self.money -= 10 * no_of_items
        else:
            plt.imshow(disgust)
            plt.show()
        
class Car:
    def __init__(self, model_name = None, fuel_rate = 0, velocity = 0, default_velocity= 0):
        self.model_name = model_name
        self.fuel_rate = fuel_rate
        self.velocity = velocity
        self.default_velocity = abs(default_velocity % 200)
        
    def run(self, distance, velocity = None):
        if not velocity:
            velocity = self.default_velocity
        # assume car can travel a distance of two mile per liter            
        remaining_distance = distance - (2 * self.fuel_rate)
        self.velocity = velocity
        if remaining_distance > 0:
            self.fuel_rate = 0
            self.stop(remaining_distance)
        else :
            self.fuel_rate -= distance / 2
            self.stop(0)
    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance :
            print(f"you couldn't make it to the destination, {remaining_distance} miles remain")
            plt.imshow(scarred)
            plt.show()
        else:
            print(f"you have arrived at your destination, your fuel rate is now {self.fuel_rate}")
            
            
    
class Employee(Person):
    def __init__(self, name = None, money = 0, mood = None, health_rate = 0,
                 id = 0, car = None, email = None, salary = 1000, distance_to_work = 0):
        Person.__init__(self, name, money, mood, health_rate)
        
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary if (salary >= 1000) else 1000
        self.distance_to_work = distance_to_work
        
    def work(self, hours):
        if hours > 8:
            self.mood = "tired"
        elif hours == 8:
            self.mood = "happy"
        else :
            self.mood = "lazy"
    
    def drive(self, distance):
        plt.imshow(driving)
        plt.show()
        self.car.run(distance)
    
    def refuel(self, litres = 100):
        self.car.fuel_rate = self.car.fuel_rate + litres if (self.car.fuel_rate + litres) <= 100 else 100
        
    def send_mail(self, to, subject, message, receiver_name):
        with open("emails.txt", "a") as emails:
            from_field = "From: " + self.email + '\n'
            to_field = "To: " + to + '\n'
            subject_field = "Subject: "+ subject + '\n'
            message_field = '\n' + f"Hi, {receiver_name}\n" + message + '\n\n'
            
            
            
            emails.writelines([from_field,
                               to_field,
                               subject_field,
                               message_field])
            
    def to_dict(self):
        return {
            "name" : self.name,
            "id" :self.id,
            "salary" : self.salary,
            "distance to work" : self.distance_to_work
            }
    
    def __repr__(self):
        return f"an employee with the name: {self.name}, and id: {self.id}"

import json            
            
class Office:
    employees_num = 0
    
    def __init__(self, name = None, employees = None):
        self.name = name
        self.employees = employees
        Office.employees_num += len(employees)
    
    def get_all_employees(self):
        return self.employees
    
    def get_employee(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                return employee
    
    def hire(self, employee):
        self.employees.append(employee)
        
    def fire(self, employee_id):
        for i in range(len(self.employees)):
            if self.employees[i].id == employee_id:
                del self.employees[i]
                return 1
        return 0
    
    def deduct(self, employee_id, deduction):
        for employee in self.employees:
            if employee.id == employee_id:
                employee.salary = employee.salary - deduction if (employee.salary - deduction) > 1000 else 1000
    
    def reward(self, employee_id, reward):
        for employee in self.employees:
            if employee.id == employee_id:
                employee.salary += reward
                
    def check_lateness(self, employee_id, move_hour, target_hour):
        for employee in self.employees:
            if employee.id == employee_id:       
                if Office.calculate_lateness(move_hour, target_hour, employee.distance_to_work, employee.default_velocity):
                    self.deduct(employee_id, 10)
                else:
                    self.reward(employee_id, 10)
                
    @staticmethod            
    def calculate_lateness(move_hour, target_hour, distance, velocity):
        time_required = distance / velocity
        return (time_required + move_hour - target_hour) > 0
    
    @classmethod
    def change_emps_num(cls, employees_num):
        cls.employess_num = employees_num
    
    def save_office_data(self):
        with open("office_data.json", "w") as office_data:
            json.dump({
                "office_name" : self.name,
                "employees" : [employee.to_dict() for employee in self.employees]
                }, office_data)
        
        
        
speedster = Car(model_name = "ferarri", fuel_rate=100, velocity = 0, default_velocity=100)
gangster = Car(model_name = "Toyota", fuel_rate=100, velocity = 0, default_velocity=60)
elder = Car(model_name = "feat", fuel_rate=100, velocity = 0, default_velocity=20)



amr = Employee(name = "amr", money = 10000, mood = "happy", health_rate=100
                ,id = 0, car = speedster, email = "amr.s.hares@gmail.com", salary = 20000
                , distance_to_work= 10)
# amr.sleep(8)

# amr.buy(10000)

# amr.drive(100)

# amr.drive(amr.distance_to_work)

# amr.drive(100)

# amr.refuel(5)
# amr.drive(10)

mohamed = Employee(name = "mohamed", money = 10000, mood = "happy", health_rate=100
                ,id = 1, car = gangster, email = "mohamed@gmail.com", salary = 10000
                , distance_to_work= 10)

mohamed.send_mail("amr.s.hares@gmail.com"
                  ,"deadline extension after following last meetup preceedings"
                  ,"the project deadline is extended to the 15th of Febuary"
                  ,"amr")      


ahmed = Employee(name = "ahmed", money = 10000, mood = "happy", health_rate=100
                ,id = 2, car = elder, email = "ahmed@gmail.com", salary = 2000
                , distance_to_work= 10)


the_office = Office(name = "the office", employees = [amr, mohamed])
print(the_office.get_all_employees())

the_office.hire(ahmed)
print(the_office.get_all_employees())

# the_office.fire(1)
# print(the_office.get_all_employees())

# print(the_office.get_employee(0).salary)
# the_office.reward(0, 1000)
# print(the_office.get_employee(0).salary)

# print(the_office.get_employee(2).salary)
# the_office.deduct(2, 1000)
# print(the_office.get_employee(2).salary)

# print(the_office.get_employee(2).salary)
# the_office.deduct(2, 600)
# print(the_office.get_employee(2).salary)
# the_office.deduct(2, 500)
# print(the_office.get_employee(2).salary)

# the_office.save_office_data()
    