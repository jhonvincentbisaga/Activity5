from abc import ABC, abstractmethod

# Base Class
class FreelanceJob(ABC):
    def __init__(self, client_name, job_title):
        self.client_name = client_name
        self.job_title = job_title

    @abstractmethod
    def calculate_earnings(self):
        pass

    def describe_job(self):
        return f"Job Title: {self.job_title}, Client: {self.client_name}"

# Subclass 1: Writing Job
class WritingJob(FreelanceJob):
    def __init__(self, client_name, job_title, word_count, rate_per_word):
        super().__init__(client_name, job_title)
        self.word_count = word_count
        self.rate_per_word = rate_per_word

    def calculate_earnings(self):
        return self.word_count * self.rate_per_word

# Subclass 2: Graphic Design Job
class GraphicDesignJob(FreelanceJob):
    def __init__(self, client_name, job_title, hours_worked, hourly_rate, revisions):
        super().__init__(client_name, job_title)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.revisions = revisions

    def calculate_earnings(self):
        base_earnings = self.hours_worked * self.hourly_rate
        bonus_for_revisions = 50 * self.revisions  # Bonus for each revision
        return base_earnings + bonus_for_revisions

# Subclass 3: Web Development Job
class WebDevelopmentJob(FreelanceJob):
    def __init__(self, client_name, job_title, project_fee, additional_features):
        super().__init__(client_name, job_title)
        self.project_fee = project_fee
        self.additional_features = additional_features

    def calculate_earnings(self):
        feature_fee = 100 * self.additional_features  # Fee for each additional feature
        return self.project_fee + feature_fee

# Function to generate invoice
def generate_invoice(job_list):
    print("Invoice:")
    for job in job_list:
        earnings = job.calculate_earnings()
        print(f"{job.describe_job()} - Earnings: ${earnings:.2f}")

# Example usage
if __name__ == "__main__":
    jobs = [
        WritingJob("Client A", "Blog Post", 1500, 0.10),
        GraphicDesignJob("Client B", "Logo Design", 10, 25, 2),
        WebDevelopmentJob("Client C", "E-commerce Site", 1200, 3)
    ]

    generate_invoice(jobs)
