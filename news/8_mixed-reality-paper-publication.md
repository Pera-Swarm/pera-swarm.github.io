---
layout: page_news
title: "Our Research Works on Mixed-Reality based Swarm Simulation has now published in the IEEE Access Journal"
description: "Under the title, 'Mixed-Reality based Multi-Agent Robotics Framework for Artificial Swarm Intelligence Experiments'"

permalink: /news/mixed-reality-simulation-framework/
parent: News
navbar_active: News
nav_order: 8

thumb: /news/img/mixed-reality-simulation-framework.png

link_url: #
link_caption: View More

author: Nuwan Jaliyagoda
published_date: 2023-10-04

resources: true
resource_list:
    - {text: 'Research Paper - IEEE Access', url: 'https://doi.org/10.1109/ACCESS.2023.3317434' }
    - {text: 'Project Page - pera-swarm.ce.pdn.ac.lk', url: 'https://pera-swarm.ce.pdn.ac.lk/projects/mr-environment-for-swarm-robotics-simulations/' }

gallery: false
gallery_images:
    - {url: '#', caption: ''}


---

Mixed Reality based Simulation Framework is one of the main outcomes of the Pera-Swarm project, and the first paper publication under the project is now published in [IEEE Access, vol. 11, 2023](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6287639) (*Impact Factor: 3.9*, 2023).

<div class="container row pt-3 pb-5">
    <div class="col-md-8 col-sm-12 col-lg-8 mx-auto">
        <img src="/news/img/mixed-reality-simulation-framework.png" class="img img-thumbnail img-fluid">
    </div>
</div>

<div class="project-section mb-5">
    <h4 class="project-section-title">Abstract</h4>
    <div class="container px-4">
        The term "Swarm intelligence" outlines a broad scope, which is generally defined as the collective behaviour of many individuals towards a certain task, each operating autonomously in a decentralised manner. Swarms are inspired by the type of biological behaviours of animals and this technology involves decentralised local control and communication, which ensures the problem-solving process is more efficient through modification and infusion into swarm robotic technology. Swarm robotics related experiments and applications are relatively expensive compared to other types of robotics experiments. The most common solution is to use computer based virtual simulations and accordingly, this study introduces a reliable and cost-effective hybrid solution using Mixed Reality (MR) technologies to perform swarm experiments on real robots and virtually deployed robots simultaneously. MR bridges the gap between the virtual and physical realms through Augmented Reality (AR) and Augmented Virtuality (AV) and addressing the weaknesses of simulators and providing a more accurate representation of real-world performance. This approach provides a platform for researchers to explore swarm robotics with enhanced realism and interactivity and conduct experiments that mimic real-world conditions. To validate this method we conducted experiments with both physical and virtual robots in near real-time in a mixed reality environment. In addition, an open-source, distributed, and modular mixed reality simulation framework was implemented with support libraries and applications. Our work not only demonstrates the potential of MR in swarm robotics but also emphasizes its value in advancing the understanding and application of swarm intelligence principles in practical contexts.
    </div>
</div>

<div class="project-section mb-2 publication-card">
    <h4 class="project-section-title">Publication</h4>
    <div class="container px-4">
    <div class="my-1 p-3 pb-4 publication-card d-none">
    <div class="row g-0">
        <div class="container">
            <div class="clearfix">
                <div class="row pt-2">
                    <div class="col d-flex flex-wrap">
                        <b><span class="text-primary research-title">{{ title }}</span></b><br>
                    </div>
                </div>
                <div class="research-authors">{{ authors }}</div>
                <i class="research-venue">{{ venue }}</i>, <span class="research-year">{{ year }}</span><br>
                <span>doi: <a class="text-muted research-doi" href="#" target="_blank">{{ doi }}</a></span>
            </div>

            <div class="row pt-2">
                <div class="col d-flex flex-wrap research-links">{{ links }}</div>
                <div class="mt-2 research-tags">{{ tags }}</div>
            </div>
        </div>
        
        <div class="publication-error d-none">
            <div class="text-center alert alert-warning m-2">
                An error occured while loading the publication information !
            </div>
        </div>
    </div>
</div>

<script>
    $(document).ready(() => {
        const API_BASE = 'https://api.ce.pdn.ac.lk/publications/v1';
        const params = new URLSearchParams(location.search);
        const doi = "10.1109/ACCESS.2023.3317434";
        const theme = params.get('theme') || 'light';
        const url = `${API_BASE}/${doi}`

        $.ajax({
            url: url,
            type: "GET",
            success: function (data) {
                console.log(url, data);

                $('title').html(data.title);
                $('.research-title').html(data.title);
                $('.research-venue').html(data.venue);
                $('.research-year').html(data.year);

                $('.research-doi').html(doi).attr('href', 'https://doi.org/' + doi);

                if (data.pdf_url != '#') {
                    $('.research-links').append(`<a class="btn-link me-2" href="${data.pdf_url}" target="_blank">[ PDF ]</a>`);
                }
                if (data.preprint_url != '#') {
                    $('.research-links').append(`<a class="btn-link me-2" href="${data.preprint_url}" target="_blank">[ PDF (Preprint) ]</a>`);
                }
                if (data.presentation_url != '#') {
                    $('.research-links').append(`<a class="btn-link me-2" href="${data.presentation_url}" target="_blank">[ Presentation ]</a>`);
                }
                if (data.project_url != '#') {
                    $('.research-links').append(`<a class="btn-link me-2" href="${data.project_url}" target="_blank">[ Project ]</a>`);
                }
                if (data.codebase != '#') {
                    $('.research-links').append(`<a class="btn-link me-2" href="${data.codebase}" target="_blank">[ Codebase ]</a>`);
                }

                // Research Tags
                const tags = (data.tags.lenght > 0) && data.tags.map((tag) => {
                    return `<span class="me-2 badge rounded-pill bg-secondary">${tag}</span>`;
                }).reduce((obj, current) => {
                    return obj + '\n' + current;
                })
                $('.research-tags').html(tags);

                // Research Authors
                const authors = data.author_info.map((author) => {
                    if (author.profile_url == '#') {
                        return `<span class="me-1">${author.name}</span>`;
                    } else {
                        return `<a class="text-decoration-none" href="${author.profile_url}" target="_blank">${author.name}</a>`;
                    }
                }).reduce((obj, current) => {
                    return obj + ', ' + current;
                })
                $('.research-authors').html(authors);

                // Show the content if every condition satisfied 
                if (data.title != '' && data.venue != '' && data.year != '' && data.author_info) {
                    $('.publication-card').removeClass('d-none');
                } else {
                    console.error("Incompleted information !")
                    $('.publication-error').removeClass('d-none');
                }


            },
            error: function (xhr, textStatus, errorThrown) {
                // Handle errors
                console.log(textStatus, errorThrown);
                $('.publication-error').removeClass('d-none');
            }
        });

    });
</script>
