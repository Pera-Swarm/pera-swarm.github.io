---
layout: page_project
title: "A GUI for Controlling and Supervising Multiple Robots Remotely"
description: "General purpose swarm robots with a GUI to monitor and control them remotely"
permalink: /projects/gui-for-controlling-and-supervising-multiple-robots/
parent: Projects
navbar_active: Projects
nav_order: 3

thumb: /projects/thumbs/gui-for-controlling.jpg

link_url: https://cepdnaclk.github.io/e15-3yp-A-GUI-for-controlling-and-supervising-multiple-robots-remotely/
link_caption: Project Blog

api_url: https://api.ce.pdn.ac.lk/projects/v1/3yp/E15/A-GUI-for-controlling-and-supervising-multiple-robots-remotely/

gallery: true
galery_images:
    - {url: '/projects/gallery/gui-for-controlling/1.jpg', caption: 'Hardware robot'}
    - {url: '/projects/gallery/gui-for-controlling/2.jpg', caption: 'Robots in the testbed'}
    - {url: '/projects/gallery/gui-for-controlling/3.jpg', caption: 'Hardware robots'}
    - {url: '/projects/gallery/gui-for-controlling/4.png', caption: 'A Screenshot of the GUI'}

resources: true
resource_list:
    - {text: 'Project Repository', url: 'https://github.com/cepdnaclk/e15-3yp-A-GUI-for-controlling-and-supervising-multiple-robots-remotely' }
    - {text: 'Project Page', url: 'https://cepdnaclk.github.io/e15-3yp-A-GUI-for-controlling-and-supervising-multiple-robots-remotely' }
    - {text: 'Technical Design', url: 'https://cepdnaclk.github.io/e15-3yp-A-GUI-for-controlling-and-supervising-multiple-robots-remotely/pdf/Technical_Design.pdf' }
    - {text: 'User Manual', url: 'https://cepdnaclk.github.io/e15-3yp-A-GUI-for-controlling-and-supervising-multiple-robots-remotely/pdf/User_Manual.pdf' }

---

According to the definition, "Swarm intelligence is the collective behavior of decentralized, self-organized systems"  Swarm robotics is applying swarm intelligence to accomplish a bigger task. And it is also similar to the behavior of animals like bees, ants, birds, etc.

One of the greatest fallbacks of swarm intelligence-related research is that it is difficult to simulate the algorithms in the real world unless you have a large number of robots to test these algorithms. Building a group of robots takes a lot of time and it is very expensive. As a solution to this problem, we can design or buy general purpose robots which have hardware capabilities to run basic swarm intelligence related algorithms. But buying a set of pre-built robots doesn’t solve the whole problem since it is too expensive yet.

The ultimate goal of this project is not only to design a common purpose swarm robot unit but also to design a platform to control and monitor them. This platform will be able to control basic functionalities of the robots such as assign a robot into a defined place, recharge the robot’s battery when it is draining out, program the robots with giving algorithms, etc… This simulation arena can be accessed from a remote location and these remote users can upload their own algorithms into the robots which are placed in the arena. After uploading, they can run it on robots and see the response of the robots using Data and Video feedback. Research teams who are working in the field of Swarm Robotics can test their algorithms without taking much effort into hardware. So it saves their time and money.
