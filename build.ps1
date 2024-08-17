$exclude = @("venv", "bot_challenge.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_challenge.zip" -Force