from core import pipeline, sandbox

def main():
    p = pipeline.Pipeline()
    s = sandbox.Sandbox(p)
    s.play()

if __name__ == "__main__":
    main()