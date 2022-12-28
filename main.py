from script.utils import ext_id, collect_mod_contents, collect_mod_id, save_env
import argparse

parser = argparse.ArgumentParser(description='Project Zomboid MOD Crawler for DockerCompose', 
                                    formatter_class=argparse.RawTextHelpFormatter)

def get_arguments():
    parser.add_argument('-p',
                        '--env_path',
                        dest='env_path',
                        help="Specify the path to save .env file", 
                        required=True, type=str)

    parser.add_argument('-u',
                        '--url',
                        dest='collection_url', 
                        help="Project Zomboid Workshop Collection URL", 
                        required=True, type=str)
    
    _args = parser.parse_args()
    return _args

def pjz_main():
    args = get_arguments()

    save_env(collect_mod_contents(collect_mod_id(ext_id(args.collection_url))), args.env_path)

    print('작업 완료되었습니다.')

if __name__ == "__main__":
    pjz_main()
