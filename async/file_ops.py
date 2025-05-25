import asyncio
import aiofiles
import os
from datetime import datetime

async def write_file(filename, content):
    """Write content to a file asynchronously"""
    async with aiofiles.open(filename, 'w') as f:
        await f.write(content)
    print(f"Written to {filename}")

async def read_file(filename):
    """Read content from a file asynchronously"""
    try:
        async with aiofiles.open(filename, 'r') as f:
            content = await f.read()
        return content
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None

async def process_files(files):
    """Process multiple files concurrently"""
    # Create some example files
    write_tasks = []
    for i, filename in enumerate(files):
        content = f"Content for file {i+1}\nCreated at {datetime.now()}\n"
        write_tasks.append(write_file(filename, content))
    
    # Write all files concurrently
    await asyncio.gather(*write_tasks)
    
    # Read all files concurrently
    read_tasks = [read_file(filename) for filename in files]
    contents = await asyncio.gather(*read_tasks)
    
    return contents

async def cleanup_files(files):
    """Clean up created files"""
    for filename in files:
        try:
            os.remove(filename)
            print(f"Removed {filename}")
        except FileNotFoundError:
            pass

async def main():
    # Example files to process
    files = [
        'file1.txt',
        'file2.txt',
        'file3.txt'
    ]
    
    try:
        # Process files
        contents = await process_files(files)
        
        # Print results
        for filename, content in zip(files, contents):
            if content:
                print(f"\nContent of {filename}:")
                print(content.strip())
        
    finally:
        # Clean up
        await cleanup_files(files)

if __name__ == "__main__":
    asyncio.run(main()) 