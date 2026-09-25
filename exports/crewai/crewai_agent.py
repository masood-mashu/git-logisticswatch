from crewai import Agent
def create_agent():
    return Agent(role='GitLogisticsWatch', goal='Autonomous Bill of Materials (BOM) Lead-Time Risk, Supplier Variance & Reorder Point Auditor Agent', backstory='Autonomous agent', verbose=True)
