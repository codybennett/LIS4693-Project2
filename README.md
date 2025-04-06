<!-- markdownlint-disable no-inline-html -->
<!-- markdownlint-disable first-line-heading  -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/codybennett/LIS4693-Project2">
    <img src="Testing Screenshot.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">LIS4693-Project2</h3>

  <p align="center">
    Project 2 for University of Oklahoma LIS4693
    <br />
    <a href="https://github.com/codybennett/LIS4693-Project2"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/codybennett/LIS4693-Project2">View Demo</a>
    ·
    <a href="https://github.com/codybennett/LIS4693-Project2/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/codybennett/LIS4693-Project2/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#running-the-streamlit-application">Running the Streamlit Application</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is an advanced information retrieval system designed for analyzing and exploring text data. It allows users to search, filter, and explore a corpus of documents interactively. The system provides tools for efficient text retrieval and document exploration without relying on artificial intelligence or machine learning techniques.

Key features include:

* **Search Functionality**: Perform keyword or phrase searches across the corpus.
* **Corpus Exploration**: Filter and explore documents interactively.
* **Export Capability**: Save the corpus or search results to a file for offline use.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

There is primarily a single dependency on the Python PANDAS package, to get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/codybennett/LIS4693-Project2.git
   ```

2. Install Python packages

   ```sh
   pipenv install
   ```

3. Generate the corpus

   Run the `data_collection.py` script to generate the corpus directory:

   ```sh
   python data_collection.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

This utility analyzes a directory of text documents (corpus). Users can:

1. **Generate Corpus**: Use the `data_collection.py` script to create the corpus from the Reuters dataset.
2. **Search**: Enter a keyword or phrase in the search bar to find relevant documents.
3. **Filter**: Use sidebar options to narrow down results by specific criteria.
4. **Explore Results**: Expand search results to view document snippets and full content.
5. **Export**: Save the corpus or search results to a text file for offline analysis.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Running the Streamlit Application

To interact with the corpus and perform searches, you can run the Streamlit application locally or access it via Streamlit Cloud:

#### Local Setup

1. Ensure all dependencies are installed:
   ```sh
   pipenv install
   ```

2. Start the Streamlit application:
   ```sh
   streamlit run streamlit_app.py
   ```

3. Open the provided URL in your browser to access the application.

#### Streamlit Cloud

The application is also deployed on [Streamlit Cloud](https://streamlit.io/cloud). You can access it directly without setting up a local environment by visiting the following link:

[Streamlit Cloud Deployment](https://streamlit.io/cloud)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GNU GPL3 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

* Cody Bennett - <codybennett@ou.edu>

Project Link: [https://github.com/codybennett/LIS4693-Project2](https://github.com/codybennett/LIS4693-Project2)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/codybennett/LIS4693-Project2.svg?style=for-the-badge
[contributors-url]: https://github.com/codybennett/LIS4693-Project2/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/codybennett/LIS4693-Project2.svg?style=for-the-badge
[forks-url]: https://github.com/codybennett/LIS4693-Project2/network/members
[stars-shield]: https://img.shields.io/github/stars/codybennett/LIS4693-Project2.svg?style=for-the-badge
[stars-url]: https://github.com/codybennett/LIS4693-Project2/stargazers
[issues-shield]: https://img.shields.io/github/issues/codybennett/LIS4693-Project2.svg?style=for-the-badge
[issues-url]: https://github.com/codybennett/LIS4693-Project2/issues
[license-shield]: https://img.shields.io/badge/license-GPLv3-blue
[license-url]: https://github.com/codybennett/LIS4693-Project2/blob/master/LICENSE.txt
