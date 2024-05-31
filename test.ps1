# Register a new user
registerUrl = "http://127.0.0.1:8000/api/register/"
headers = { "Content-Type" = "application/json" }
body = {
    username = "testuser"
    password = "password"
} | ConvertTo-Json

response = Invoke-RestMethod -Uri $registerUrl -Method Post -Headers $headers -Body $body
Write-Output "Registration Response:"
response

# Login to get a JWT token
$loginUrl = "http://127.0.0.1:8000/api/login/"
$body = @{
    username = "testuser"
    password = "password"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri $loginUrl -Method Post -Headers $headers -Body $body
Write-Output "Login Response:"
$response

# Extract tokens from the response
$accessToken = $response.access
$refreshToken = $response.refresh

# Access a protected route
$protectedUrl = "http://127.0.0.1:8000/api/protected/"
$headers = @{
    "Authorization" = "Bearer $accessToken"
}

$response = Invoke-RestMethod -Uri $protectedUrl -Method Get -Headers $headers
Write-Output "Protected Route Response:"
$response
