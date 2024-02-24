# Quorum Coding Challenge

#### Working with legislative data

---



1 - Discuss your application implementation strategy and decisions. Please consider the time
complexity, cost of effort, technologies used and any other variable you understand
important in your development process.

---
> In the implementation strategy, I chose to use the Django REST Framework (DRF) in conjunction with Django to create
> RESTful APIs on the backend. This decision was made due to the robustness and flexibility offered by DRF, allowing easy
> implementation of endpoints for communication between the frontend and backend. And it's the framework I'm most skilled
> at. On the frontend, I chose Next.js because of its server-side rendering (SSR) capabilities and static page generation.
> This significantly improves application performance, reducing page loading times and improving the user experience. And
> it's so simple to understand that even though it's my first time using it, I didn't have any difficulties. This approach
> of using Django with DRF on the backend and Next.js on the frontend provides a solid and scalable
> architecture for the application. Additionally, both technologies have extensive documentation and an active community,
> which facilitates long-term development and maintenance.
___

2 - How would you change your solution to account for future columns that could be
requested, such as “Bill voted on date” or “Co-sponsors”?

___

> I created dynamic models, their attributes are generated from data sources. Depending on the decision of which data
> source to use, some adjustment may be necessary, but due to the way the model was structured, the effort should be
> minimal.
___

3 - How would you change your solution if instead of receiving CSVs of data, you received a
list of legislators or bills for which you should generate a CSV?

___

> I followed some design patterns such as Strategy and Factory Method and made use of SOLID principles, making the code
> easy to maintain and extend.

---

4 - How long did you spend working on the task?

___

> Between coming and going from my daily duties, I think it took me approximately 5 hours. I evolved the code little by
> little, adjusting, improving until I considered the solution acceptable.



