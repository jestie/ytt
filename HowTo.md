# How to Use the YouTube Transcript Extractor

This document provides detailed instructions on how to use the YouTube Transcript Extractor application.

## Prerequisites

-   Python 3.x
-   `pip` (Python package installer)

## Installation

1.  **Clone the Repository:**

    -   Open your terminal or command prompt.
    -   Navigate to the directory where you want to clone the repository.
    -   Run the following command:

        ```bash
        git clone [your_repository_url]
        cd [your_project_directory]
        ```

2.  **Install Dependencies:**

    -   Navigate to the project directory.
    -   Run the following command to install the required Python packages:

        ```bash
        pip install -r requirements.txt
        ```

## Running the Application

1.  **Start the Flask Server:**

    -   In your terminal, navigate to the project directory.
    -   Run the following command to start the Flask development server:

        ```bash
        python app.py
        ```

    -   The server will start, and you'll see a message indicating the URL where the application is running (e.g., `http://127.0.0.1:4000`).

2.  **Access the Application:**

    -   Open your web browser.
    -   Enter the URL displayed in the terminal into the address bar.
    -   The YouTube Transcript Extractor interface will load.

## Using the Application

1.  **Enter YouTube URL:**

    -   In the input field, enter the URL of the YouTube video for which you want to extract the transcript.

2.  **Fetch Transcript:**

    -   Click the "Fetch Transcript" button.

3.  **View Transcript:**

    -   The transcript will be displayed in the transcript window.
    -   If the video has no transcripts or an error occurs, an error message will be displayed.

## Troubleshooting

-   **"Failed to retrieve transcript." Error:**
    -   Ensure the YouTube video has transcripts available.
    -   Check the `logs/app.log` file for detailed error messages.
    -   Verify your internet connection.
-   **"ModuleNotFoundError: No module named 'youtube_transcript_api'" Error:**
    -   Run `pip install youtube-transcript-api` to install the required library.
-   **Logo not showing:**
    -   Make sure that logo.png is inside the static folder.
-   **Page not loading:**
    -   Make sure that the app.py file is running.
    -   Make sure that the index.html file is inside the static folder.

## Contact

For further assistance, please contact [Your Contact Information].