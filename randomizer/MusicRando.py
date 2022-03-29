"""Randomize Music passed from Misc options."""
import gzip
import json
import random
from ast import And

import js

import randomizer.Lists.Exceptions as Ex
from randomizer.Enums.SongType import SongType
from randomizer.Lists.Songs import Song, SongGroup, song_data
from randomizer.Patcher import ROM
from randomizer.Settings import Settings
from randomizer.Spoiler import Spoiler


def randomize_music(spoiler: Spoiler):
    """Randomize music passed from the misc music settings.

    Args:
        settings (Settings): Settings object from the windows form.
    """
    settings: Settings = spoiler.settings
    # Check if we have anything beyond default set for BGM
    if settings.music_bgm != "default":
        # If the user selected standard rando
        if settings.music_bgm == "randomized":

            # These lines exist for testing only
            # file = open('static/patches/pointer_addresses.json')
            # pointer_addresses = json.load(file)

            # Generate the list of BGM songs
            song_list = []
            for song in song_data:
                if song.type == SongType.BGM:
                    # For testing, flip these two lines
                    # song_list.append(pointer_addresses[0]["entries"][song_data.index(song)])
                    song_list.append(js.pointer_addresses[0]["entries"][song_data.index(song)])

            ShuffleMusicWithSizeCheck(spoiler, song_list)

        # If the user was a poor sap and selected chaos put DK rap for everything
        elif settings.music_bgm == "chaos":
            # Find the DK rap in the list
            rap = js.pointer_addresses[0]["entries"][song_data.index(next((x for x in song_data if x.name == "DK Rap"), None))]
            # Find all BGM songs
            song_list = []
            for song in song_data:
                if song.type == SongType.BGM:
                    song_list.append(js.pointer_addresses[0]["entries"][song_data.index(song)])

            # Load the DK Rap song data
            ROM().seek(rap["pointing_to"])
            stored_data = ROM().readBytes(rap["compressed_size"])
            uncompressed_data_table = js.pointer_addresses[26]["entries"][0]
            # Replace all songs as the DK rap
            for song in song_list:
                ROM().seek(song["pointing_to"])
                ROM().writeBytes(stored_data)
                # Update the uncompressed data table to have our new size.
                ROM().seek(uncompressed_data_table["pointing_to"] + (4 * song_list.index(song)))
                new_bytes = ROM().readBytes(4)
                ROM().seek(uncompressed_data_table["pointing_to"] + (4 * song_list.index(rap)))
                ROM().writeBytes(new_bytes)
        elif settings.music_bgm == "uploaded":
            # Generate the list of BGM songs
            song_list = []
            for song in song_data:
                if song.type == SongType.BGM:
                    song_list.append(js.pointer_addresses[0]["entries"][song_data.index(song)])

            # Load our BGM data and just shuffle it around
            added_bgm = list(js.cosmetics.bgm)
            random.shuffle(added_bgm)

            already_modified = []
            for item in added_bgm:

                def check_song():
                    random_song = random.choice(song_list)
                    # Exit loop for recursion
                    if len(already_modified) >= len(song_list):
                        return
                    if random_song not in already_modified:
                        ROM().seek(random_song["pointing_to"])
                        ROM().writeBytes(gzip.compress(bytes(item), compresslevel=9))
                        already_modified.append(random_song)
                    else:
                        check_song()

                check_song()
            duped_song_list = song_list.copy()
            random.shuffle(duped_song_list)
            shuffle_music(song_list, duped_song_list)
    # If the user wants to randomize fanfares
    if settings.music_fanfares != "default":
        # Check if our setting is just rando
        if settings.music_fanfares == "randomized":
            # Load the list of fanfares
            fanfare_list = []
            for song in song_data:
                if song.type == SongType.Fanfare:
                    fanfare_list.append(js.pointer_addresses[0]["entries"][song_data.index(song)])

            # Shuffle the fanfare list
            ShuffleMusicWithSizeCheck(spoiler, fanfare_list)

        elif settings.music_fanfares == "uploaded":
            # Generate the list of fanfares songs
            song_list = []
            for song in song_data:
                if song.type == SongType.Fanfare:
                    song_list.append(js.pointer_addresses[0]["entries"][song_data.index(song)])

            # Load our fanfares data and just shuffle it around
            added_fanfares = list(js.cosmetics.fanfares)
            random.shuffle(added_fanfares)

            already_modified = []
            for item in added_fanfares:

                def check_song():
                    random_song = random.choice(song_list)
                    # Exit loop for recursion
                    if len(already_modified) >= len(song_list):
                        return
                    if random_song not in already_modified:
                        ROM().seek(random_song["pointing_to"])
                        ROM().writeBytes(gzip.compress(bytes(item), compresslevel=9))
                        already_modified.append(random_song)
                    else:
                        check_song()

                check_song()
            duped_song_list = song_list.copy()
            random.shuffle(duped_song_list)
            shuffle_music(song_list, duped_song_list)

    # If the user wants to randomize events
    if settings.music_events != "default":
        # Check if our setting is just rando
        if settings.music_events == "randomized":
            # Load the list of events
            event_list = []
            for song in song_data:
                if song.type == SongType.Event:
                    event_list.append(js.pointer_addresses[0]["entries"][song_data.index(song)])

            # Shuffle the event list
            ShuffleMusicWithSizeCheck(spoiler, event_list)


def ShuffleMusicWithSizeCheck(spoiler: Spoiler, song_list: list):
    """Facilitate shuffling of music."""
    retries = 0
    while True:
        try:
            # Copy the existing list of songs and shuffle it
            vanilla_music = song_list.copy()
            shuffled_music = song_list.copy()
            random.shuffle(shuffled_music)
            vanilla_song_list = []
            new_song_list = []
            song_map_vanillaTotalSize = {}
            song_map_newTotalSize = {}
            while len(vanilla_music) > 0:
                song_item = vanilla_music.pop(0)
                vanillaSong: Song = song_data[song_item["index"]]
                newSong: Song = None
                for shuffled_song_item in shuffled_music:
                    newSong: Song = song_data[shuffled_song_item["index"]]
                    # BGM has groups to control size of assigned songs
                    if vanillaSong.group is not None and vanillaSong.type == SongType.BGM:
                        groupName = SongGroup(vanillaSong.group).name
                        if groupName not in song_map_vanillaTotalSize:
                            song_map_vanillaTotalSize[groupName] = 0
                        if groupName not in song_map_newTotalSize:
                            song_map_newTotalSize[groupName] = 0
                        if SongGroup(vanillaSong.group) == SongGroup.Self:
                            if shuffled_song_item["uncompressed_size"] > song_item["uncompressed_size"]:
                                continue
                        else:
                            # If the new size exceeds the vanilla size, pick a different song
                            if (song_map_newTotalSize[groupName] + shuffled_song_item["uncompressed_size"]) > (song_map_vanillaTotalSize[groupName] + song_item["uncompressed_size"]):
                                continue
                        song_map_vanillaTotalSize[groupName] += song_item["uncompressed_size"]
                        song_map_newTotalSize[groupName] += shuffled_song_item["uncompressed_size"]
                    # Fanfares have different rule for limiting size
                    elif vanillaSong.type == SongType.Fanfare:
                        if shuffled_song_item["uncompressed_size"] > song_item["uncompressed_size"] * 1.5:
                            continue
                    # If it gets this far, the assignment is good
                    shuffled_music.remove(shuffled_song_item)
                    vanilla_song_list.append(song_item)
                    new_song_list.append(shuffled_song_item)

                    # Write to spoiler
                    if vanillaSong.type == SongType.BGM:
                        spoiler.music_bgm_data[vanillaSong.name] = newSong.name
                    elif vanillaSong.type == SongType.Fanfare:
                        spoiler.music_fanfare_data[vanillaSong.name] = newSong.name
                    elif vanillaSong.type == SongType.Event:
                        spoiler.music_event_data[vanillaSong.name] = newSong.name

                    break
                else:
                    raise Ex.MusicPlacementExceededMapThreshold

            print(song_map_vanillaTotalSize)
            print(song_map_newTotalSize)
            # For testing, comment out shuffle_music
            shuffle_music(vanilla_song_list, new_song_list)
            return
        except Ex.MusicPlacementExceededMapThreshold:
            if retries == 20:
                print("Music rando failed, out of retries.")
                raise Ex.MusicAttemptCountExceeded
            else:
                retries += 1
                print("Music rando failed. Retrying. Tries: " + str(retries))
                # Reset spoiler object
                if vanillaSong.type == SongType.BGM:
                    spoiler.music_bgm_data = {}
                elif vanillaSong.type == SongType.Fanfare:
                    spoiler.music_fanfare_data = {}
                elif vanillaSong.type == SongType.Event:
                    spoiler.music_event_data = {}


def shuffle_music(pool_to_shuffle, shuffled_list):
    """Shuffle the music pool based on the OG list and the shuffled list.

    Args:
        pool_to_shuffle (list): Original pool to shuffle.
        shuffled_list (list): Shuffled order list.
    """
    uncompressed_data_table = js.pointer_addresses[26]["entries"][0]
    stored_song_data = {}
    stored_song_sizes = {}
    # For each song in the shuffled list, randomize it into the pool using the shuffled list as a base
    # First loop over all songs to read data from ROM
    for song in pool_to_shuffle:
        ROM().seek(song["pointing_to"])
        stored_data = ROM().readBytes(song["compressed_size"])
        stored_song_data[song["index"]] = stored_data
        # Update the uncompressed data table to have our new size.
        ROM().seek(uncompressed_data_table["pointing_to"] + (4 * song["index"]))
        new_bytes = ROM().readBytes(4)
        stored_song_sizes[song["index"]] = new_bytes

    # Second loop over all songs to write data into ROM
    for song in pool_to_shuffle:
        shuffled_song = shuffled_list[pool_to_shuffle.index(song)]
        song_data = stored_song_data[shuffled_song["index"]]
        ROM().seek(song["pointing_to"])
        ROM().writeBytes(song_data)
        # Update the uncompressed data table to have our new size.
        song_size = stored_song_sizes[shuffled_song["index"]]
        ROM().seek(uncompressed_data_table["pointing_to"] + (4 * song["index"]))
        ROM().writeBytes(song_size)