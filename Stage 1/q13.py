def main():
    count = 0
    for i in range(60):
        for j in range(60):
            for k in range(100):
                time = set(f"{k:02d}{j:02d}{i:02d}")
                if len(time) == 2:
                    print(f"{k:02d}:{j:02d}:{i:02d}")
                    count += 1
                    
    print(count)

if __name__ == "__main__":
    main()