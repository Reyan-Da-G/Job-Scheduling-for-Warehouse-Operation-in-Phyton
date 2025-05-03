
/*
-------------------------------------------------------------------------------------------------------
               
               Project title   : Job Scheduling for Warehouse Operation
               Made By         : Muhammad Reyan, Ayesha Akmal and Zuha Bashir
               Language used   : Phyton
               Platform        : Windows 11 
               IDE used        : Visual Studio Code
               Date completed  : 2025-05-01
               Contet          : This project implements job scheduling for warehouse operations (SJF) non-preemptive algorithm."
 

 ------------------------------------------------------------------------------------------------------
*/




import matplotlib.pyplot as plt
from tabulate import tabulate

def sjf_non_preemptive(jobs):
    """
    Simulates the SJF Non-Preemptive Scheduling Algorithm with Gantt chart.

    Args:
        jobs (list): List of jobs with name, arrival time, and burst time.

    Returns:
        tuple: Scheduled jobs, average waiting time, average turnaround time.
    """

    # Sort jobs by arrival time and burst time
    jobs.sort(key=lambda x: (x['arrival'], x['burst']))

    time = 0
    completed = []
    waiting_time = 0
    turnaround_time = 0
    gantt_chart = []

    while jobs:
        available_jobs = [job for job in jobs if job['arrival'] <= time]
        
        if not available_jobs:
            time = jobs[0]['arrival']
            continue

        current = min(available_jobs, key=lambda x: x['burst'])
        jobs.remove(current)

        start_time = time
        time += current['burst']
        completion_time = time

        wt = start_time - current['arrival']
        tat = completion_time - current['arrival']

        waiting_time += wt
        turnaround_time += tat

        # Store the execution details
        completed.append({
            'Job': current['name'],
            'Arrival Time': current['arrival'],
            'Burst Time': current['burst'],
            'Start Time': start_time,
            'Completion Time': completion_time,
            'Waiting Time': wt,
            'Turnaround Time': tat
        })

        # For Gantt chart
        gantt_chart.append((current['name'], start_time, completion_time))

    # Averages
    n = len(completed)
    avg_wt = waiting_time / n
    avg_tat = turnaround_time / n

    # Display table
    print("\n📋 Scheduled Jobs Table:\n")
    print(tabulate(completed, headers="keys", tablefmt="fancy_grid"))

    print("\n📊 Performance Metrics:")
    print(f"➡️ Average Waiting Time   : {avg_wt:.2f} units")
    print(f"➡️ Average Turnaround Time: {avg_tat:.2f} units")

    # Gantt Chart
    plot_gantt_chart(gantt_chart)

    return completed, avg_wt, avg_tat

def plot_gantt_chart(gantt_data):
    """
    Plots a Gantt chart using matplotlib.

    Args:
        gantt_data (list): List of (job_name, start_time, end_time) tuples.
    """
    fig, ax = plt.subplots(figsize=(10, 2))
    for i, (job, start, end) in enumerate(gantt_data):
        ax.barh(0, end - start, left=start, label=job)
        ax.text((start + end) / 2, 0, job, ha='center', va='center', color='white', fontsize=9, fontweight='bold')
    
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title("🕒 Gantt Chart - SJF (Non-Preemptive)")
    ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.tight_layout()
    plt.show()

def get_jobs_from_user():
    """
    Get job data from user input.
    
    Returns:
        list: List of jobs entered by the user.
    """
    jobs = []
    n = int(input("🔢 Enter the number of jobs: "))
    print("📥 Enter job details below:")

    for i in range(n):
        name = input(f"\n➡️ Job {i+1} name: ")
        arrival = int(input("   Arrival Time: "))
        burst = int(input("   Burst Time: "))
        jobs.append({'name': name, 'arrival': arrival, 'burst': burst})
    
    return jobs

# 🚀 Main Execution
if __name__ == "__main__":
    user_jobs = get_jobs_from_user()
    sjf_non_preemptive(user_jobs)
