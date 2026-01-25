
install:
	bundle install

serve: clean
	bundle exec jekyll serve --livereload --incremental --force-polling

# 'make build' etc..
build: clean
	bundle exec jekyll build

test:
	cd tests; python3 -m unittest discover -v -f


clean:
	rm -rf _site

emptyCommit:
	git pull
	git commit --allow-empty -m "Empty commit (Force rebuild)"
	git push

run: clean
	bundle exec jekyll serve --livereload --incremental