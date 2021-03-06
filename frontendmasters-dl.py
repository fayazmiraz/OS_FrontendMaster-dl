import click
from extractor.spider import Spider

@click.command()
@click.option('--course', prompt='Course ID', help='Course ID (e.g. `firebase-react`)')
@click.option('--id', prompt='Username', help='Frontend Master Username')
@click.option('--password', prompt='Password', help='Frontend Master Password')
@click.option('--mute-audio', help='Mute Frontend Master browser tab', is_flag=True)
def downloader(id, password, course, mute_audio):
    spider = Spider(mute_audio)
    click.secho('>>> Login with your credential', fg='green')
    spider.login(id, password)

    click.secho('>>> Downloading course: ' + course, fg='green')
    spider.download(course)

    click.secho('>>> Download Completed! Thanks for using frontendmasters-dl', fg='green')

# TODO: (Xinyang) Switching to setuptools
#   http://click.pocoo.org/5/quickstart/#switching-to-setuptools
if __name__ == '__main__':
    downloader()
