# Solution ACME exercise
##  Overview of the solution

First of all, I had to analyze what was the output desired, and how to made this with an optimal solution. After of analyzed some paths to the solution, the best decision decided to follow OOP paradigm, and MVC architecture to separate the business logic (the controllers) of the models. Last, but not least important, the solution was made following the SOLID principles, that allowed me to write more clean code.  


## Explanation of the architecture

After of an analisis of the expected solution, I decided that this has to follow the OOP paradigm because, this allow that the code can be reutilized, organized and easy to mantain. Even, this paradigm follows the principle DRY, that avoid the code duplication and make eficents programs. 
Also, I tried that the solution can get a more simplified way of be understood by others, so I separate the classes and packages into models and controller, following the MVC architecture was the better option. With this, the program logic was separated of the models, reducing the coupling.

## Explanation of the approach and methodology
1. List the requirements of the solution
2. Create a UML diagram to represent the entities and responsabilities of each one.
3. List the options of technologies, languages and other options that can be used.
4. Choose the best options from the previous step
   - Object oriented programming allows a better design of the entities, which are schedule and employee. 
   - Use of MVC model, allowing a better understanding of the order of the code segments, separating responsibilities between them.
   - Follow SOLID principles at each stage of development.
5. Implement tests to validate that the solution works correctly, as expected. 

### UML Diagram

![UML Diagram_ACME solution](https://user-images.githubusercontent.com/66764846/216175016-a46e92ef-0d7f-4f34-9e84-f4aa84355c74.png)


## How to run locally

- Clone the repository
   ```
   git clone https://github.com/hayleencc/ioet_exercise.git
   cd ioet_exercise
   ```
   
 - Create a virtual environment in the root folder of the project
   ```
   python3 -m venv venv
   ```
      If you have some trouble you can try with with:
      ```
      python -m venv venv
      ```
  
  - Activate the virtual enviroment    
       _For linux/MacOS users:_ 
     ```
      source venv/bin/activate
     ```
     
       _For windows users:_ 
     ```
      \venv\Scripts\activate
     ```
   
  - Install the dependencies   
      ```
     pip3 install -r requirements.txt
     ```
     
  - Run the project  
      ```
     python main.py 
     ```
     
   - Run tests 
      ```
     pytest
     ```
 
 
