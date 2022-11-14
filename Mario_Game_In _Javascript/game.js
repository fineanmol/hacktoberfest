
onload = function () {
    steps = 16;
    move_step = steps * 5;
    fly_step = steps * 15;
    ground_height = 0;
    asset_height = 16;
    platforms_array = [];
    moves = [];
    profit = [];
    pos = 0;
    onGround = true;

    BootState = {
        init : function () {
            game.stage.backgroundColor = '#5c94fc';
            game.scale.scaleMode = Phaser.ScaleManager.SHOW_ALL;
            // game.scale.pageAlignHorizontally = true;
            // game.scale.pageAlignVertically = true;
        },
        create : function () {
            this.state.start("PreloadState");
        }
    };

    PreloadState = {
        preload : function () {
            game.load.spritesheet('enemy', 'assets/goomba_nmbtds.png', 16, 16);
            game.load.spritesheet('mario', 'assets/mario_wjlfy5.png', 16, 16);
            game.load.spritesheet('coin', 'assets/coin_iormvy.png', 16, 16);
            game.load.spritesheet('flag', 'assets/flag.png', 33, 168);
            game.load.image('cloud', 'assets/cloud.png');
            game.load.image('grass', 'assets/grass.png');
            game.load.image('tile', 'assets/tile.png');
            game.load.image('pipe1', 'assets/pipe1.gif');
            game.load.image('pipe2', 'assets/pipe2.gif');
            game.load.image('castle', 'assets/castle.gif');
            game.load.image('ground', 'assets/ground.png');
        },
        create : function () {
            this.state.start("GameState")
        }
    };
    GameState = {
        init: function() {
            createGame();
        },
        update: function() {
            updateState();
        }
    };

    function createGame() {

        platforms_array = [];
        moves = [];
        profit = [];

        game.world.setBounds(0,0,game_length,game_height);
        game.physics.startSystem(Phaser.Physics.ARCADE);

        ground_height = game.height - 2*asset_height;
        clouds = game.add.group();
        change = 15;
        for (var i = 70; i < game_length; i+= 240) {
            clouds.create(i, change + game.height / 6, 'cloud');
            change *= -1;
        }

        grass = game.add.group();
        for (var i = 130; i < game_length; i+= 290) {
            grass.create(i, ground_height - steps, 'grass');
        }

        ground = game.add.tileSprite(0,ground_height, game_length, game.height, 'ground');
        game.physics.arcade.enable(ground);
        ground.body.immovable = true;

        coins = game.add.group();
        coins.enableBody = true;

        goombas = game.add.group();
        goombas.enableBody = true;

        flag = game.add.sprite(1500, ground_height-168, 'flag');
        flag.animations.add('celebrate');

        game.add.sprite(300, ground_height-64, 'pipe2');
        game.add.sprite(560, ground_height-132, 'castle').scale.setTo(0.75,0.75);
        game.add.sprite(900, ground_height-128, 'pipe1');
        game.add.sprite(1200, ground_height-80, 'pipe2').scale.setTo(1.25,1.25);

        platforms = game.add.group();
        platforms.enableBody = true;
        for (i = 0; i < 5; i++) {
            platforms_array.push([i * 300 + 60]);
            var cnt1=0, cnt2=0;
            for(j=0;j<8;j++) {
                var pos = i * 300 + j*asset_height + 100;
                var platform = platforms.create(pos, ground_height - 60, 'tile');
                platform.body.immovable = true;

                if(j===2 || j===7){
                    if(Math.random()>0.5) {
                        var goomba = goombas.create(pos, ground_height - asset_height - 60, 'enemy');
                        goomba.animations.add('walk', [0, 1]);
                        goomba.animations.play('walk', 2, true);
                    }
                    if(Math.random()>0.5) {
                        goomba = goombas.create(pos, ground_height - asset_height, 'enemy');
                        goomba.animations.add('walk', [0, 1]);
                        goomba.animations.play('walk', 2, true);
                    }
                } else{
                    if(Math.random()>0.5){
                        var coin = coins.create(pos, ground_height - asset_height - 60, 'coin');
                        coin.animations.add('spin', [0,0,1,2]);
                        coin.animations.play('spin', 3, true);
                        cnt1++;
                    }
                    if(Math.random()>0.5){
                        var coin = coins.create(pos, ground_height - asset_height, 'coin');
                        coin.animations.add('spin', [0,0,1,2]);
                        coin.animations.play('spin', 3, true);
                        cnt2++;
                    }
                }
            }
            profit.push([cnt1, cnt2]);
        }

        player = game.add.sprite(16, game.height - 72, 'mario');
        game.physics.arcade.enable(player);
        player.body.gravity.y = 370;
        player.body.collideWorldBounds = true;
        player.animations.add('walkRight', [1, 2, 3], 10);
        player.goesRight = true;
        player.body.enable = false;

        temptext.innerText = text + getString() + text2;
    }

    function getString(){
        ret = '';
        tmp = [];
        for(i=0;i<5;i++)
            ret = ret + '['+String(profit[i][0])+','+String(profit[i][1])+'] ';
        ret = '[ '+ret+']\n';
        return ret;
    }

    function updateState() {
        game.physics.arcade.collide(player, ground, groundOverlap);
        game.physics.arcade.collide(player, platforms);
        game.physics.arcade.collide(goombas, ground);
        game.physics.arcade.overlap(player, goombas, goombaOverlap);
        game.physics.arcade.overlap(player, coins, coinOverlap);
        game.camera.follow(player, Phaser.Camera.FOLLOW_TOPDOWN);

        if (player.body.enable) {

            player.body.velocity.x = move_step;
            player.play('walkRight');
            if (player.x+steps >= platforms_array[pos]){
                if( moves[pos] === "1" && onGround) {
                    onGround = false;
                    player.body.velocity.y = -fly_step;
                    player.animations.stop();
                }
                pos++;
            }

            if (player.body.velocity.y != 0) {
                if (player.goesRight) player.frame = 5;
                else player.frame = 12;
            }

            if(player.x >= 1490 && player.y===ground_height-player.height) {
                player.body.enable = false;
                flag.animations.play('celebrate', 5);
            }
        }
    }

    function groundOverlap() {
        onGround = true;
    }

    function coinOverlap(player, coin) {
        coin.kill();
    }

    function goombaOverlap(player, goomba) {
        goomba.animations.stop();
        goomba.frame = 2;
        goomba.body.enable = false;
        player.body.velocity.y = -fly_step/2;
        game.time.events.add(Phaser.Timer.SECOND, function() {
            goomba.kill();
        });
    }

    var refresh = document.getElementById('generate-graph');
    refresh.onclick = function () {
        game.state.start("GameState");
    };
    text = 'You\'ll receive a 2D array as input. Each column stores rewards on higher and lower platform. ' +
        'You have to return an array stating 1 if you want to jump to higher platform, 0 otherwise. However, ' +
        'after selecting 1 you have to select 0 the next time. Can you solve it ?\n';
    text2 = 'Click on solve to get solution';
    var temptext = document.getElementById('temptext');
    var solve = document.getElementById('solve');

    solve.onclick = function () {

        ans1 = profit[0][0];
        ans2 = profit[0][1];
        tmp = [];
        ans = '';
        for(i=1;i<5;i++){
            console.log(ans1,ans2);
            tans1 = ans2+profit[i][0];
            if(ans1>ans2)
                tmp.push(1);
            else
                tmp.push(0);
            tans2 = profit[i][1]+Math.max(ans1,ans2);
            ans1 = tans1;
            ans2 = tans2;
        }
        prev = -1;
        if(ans1>ans2)
            prev = 1;
        else
            prev = 0;

        console.log(ans1,ans2,tmp);
        tpos = 3;
        while(tpos>=0){
            ans = String(prev)+' '+ans;
            if(prev===1){
                prev = 0;
            } else{
                prev = tmp[tpos];
            }
            tpos--;
        }
        if(prev===1)
            ans = '1 '+ans;
        else
            ans = '0 '+ans;
        temptext.innerText = temptext.innerText + '\n' + ans;
        moves = ans.split(' ');
        pos = 0;
        console.log(moves);
        player.body.enable = true;
    };


    screen_width = window.document.getElementById("mynetwork").innerWidth;
    game_length = 1550;
    game_height = window.document.getElementById("mynetwork").innerHeight;
    game = new Phaser.Game(320, 240, Phaser.AUTO, 'mynetwork');
    game.state.add("BootState",BootState);
    game.state.add("PreloadState",PreloadState);
    game.state.add("GameState",GameState);
    game.state.start("BootState");
};
