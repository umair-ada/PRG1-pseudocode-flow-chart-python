print("=== Social Media Influence Calculator ===")
    
# Input
username = input("Enter your username: ")
followers_count = int(input("Enter your follower count: "))
posts_count = int(input("Enter number of recent posts to analyse: "))

engagement_score = 0

# Iteration through posts
for i in range(posts_count):
    print(f"\nPost {i+1}:")
    likes_on_post = int(input("Enter likes on this post: "))
    comments_on_post = int(input("Enter comments on this post: "))
    
    post_engagement = likes_on_post + (comments_on_post * 2)
    engagement_score += post_engagement

# Calculations
average_engagement = engagement_score / posts_count
influence_rating = (followers_count * average_engagement) / 1000

# Selection for status determination
if influence_rating >= 10000:
    status = "Mega Influencer"
    rate_per_post = 5000
elif influence_rating >= 1000:
    status = "Rising Influencer"
    rate_per_post = 500
elif influence_rating >= 100:
    status = "Micro Influencer"
    rate_per_post = 50
else:
    status = "Getting Started"
    rate_per_post = 0

# Output
print(f"\n{username}, you are a: {status}")
print(f"Your influence score: {influence_rating:.1f}")

if rate_per_post > 0:
    print(f"Potential earnings per sponsored post: £{rate_per_post}")
else:
    print("Keep posting! You'll get there!")