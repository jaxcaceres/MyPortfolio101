# Simple Resume Generator
def create_resume():
    print("=" * 50)
    print("          PROFESSIONAL RESUME")
    print("=" * 50)
    
    # Personal Info
    name = input("Enter your full name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    location = input("Enter your location: ")
    
    print("\n" + "-" * 50)
    print(f"{name.upper()}")
    print(f"{email} | {phone} | {location}")
    print("-" * 50)
    
    # Summary
    print("\nPROFESSIONAL SUMMARY")
    summary = input("Write a short professional summary: ")
    print(summary)
    
    # Skills
    print("\nTECHNICAL SKILLS")
    skills = input("Enter skills (comma separated): ").split(",")
    for skill in skills:
        print(f"• {skill.strip()}")
    
    # Experience
    print("\nPROFESSIONAL EXPERIENCE")
    while True:
        company = input("\nCompany name (or type 'done'): ")
        if company.lower() == "done":
            break
        role = input("Job title: ")
        dates = input("Dates (e.g. 2022 - Present): ")
        print(f"\n{role} | {company}")
        print(dates)
        
        print("Bullet points (type 'next' when finished):")
        while True:
            bullet = input("• ")
            if bullet.lower() == "next":
                break
            print(f"  - {bullet}")
    
    print("\n" + "=" * 50)
    print("Resume generated successfully!")
    print("=" * 50)

# Run it
create_resume()
